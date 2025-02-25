# ##################################################################
# PeoPle(lovers.cgi)
#    $ver = '1.6';
# Copyright (C) 2002 Missing Link.
# All rights reserved.
# 작성자 Sho
# E-mail: sho@area-s.com
# Home Page: http://www.area-s.com/
# 이 스크립트는 프리웨어 입니다.
# 본 스크립트를 이용하는 분은 이하의 URL에 기재된
# 이용규정에 동의 한 것으로 간주합니다.
# http://www.area-s.com/main/rule.html
# 저작권은 MISSING LINK가 보유합니다.
# 질문등은 서포트 게시판에서만 받습니다.
# http://www.area-s.com/main/support.html
# ##################################################################

# ########################## 데이터 개시 ###########################
# 이하의 항목은 보통 변경 불필요

# 애완동물이 상대의 집의 애완동물에게 취하는 행동(예：○○「와 놀았다」)
@IPC = ('(을/를) 때렸다','(와/과) 놀았다','(와/과) 외출했다','에게 선물을 줬다','(와/과) 장난쳤다');
# 상대의 애완동물이 자신의 집의 애완동물에게 취하는 행동(위와대칭. 예：○○은 ○○「와 놀았습니다」)
@UPC = ('에게 얻어맞았다','(와/과) 놀았다','(와/과) 외출했다','에게 선물을 받았다','(와/과) 장난쳤다');

# ########################## 데이터 종료 ###########################

# Sub Lovers #
sub lovers {
    # 자신의 연인 리스트
    @ilv = map  { [split(/,/)] } split(/△/,$lv);

    return if !@ilv;

    $no     = int(rand(@ilv));
    return if !&get_uuser($ilv[$no][0]);         # 랜덤으로 선택한 연인의 데이터를 취득
    $imatch = &love_match($uv,$uiv);             # 상대가 자신의 취향인가 체크
    $umatch = &love_match($uuv,$iv);             # 자신이 상대의 취향인가 체크
    $match2 = $imatch + $umatch;                 # 두사람의 궁합

    # 상대의 연인 리스트
    %ulv = map  { $_->[0] => [@$_] }
           map  { [split(/,/)] } split(/△/,$ulv);

    $dice = int(rand(200)) + 1 + ($def_dv * 10);
    $lvht = $dice <= $match2 ? 1 : 0;

    &name_title($usx,$sx);

    $ilv = \$ilv[$no][3];
    $ulv = \$ulv{"$id"}[3];

    if ($upg) {
        if ($uhw eq $id) {
            &msg("아기의 탄생을 기대하고 있습니다");
            $shy = 1;
            return;
        }
        else {
            &msg("$unm$unt이 누군가의 아이를 임신한 것 같습니다");
            &msg("$nm$int은 $unm$unt에게서 몸을 사립니다");
            &add_record("$nm$int은 $unm$unt에게서 몸을 사립니다");
            &add_record("$nm$int은 $unm$unt에게서 몸을 사립니다",'other');
            &add_news("$nm$int이 $unm$unt에게서 몸을 사립니다");
            splice(@ilv,$no,1);
            delete $ulv{"$id"};
            $blue = 1; $lp--; $fc = 1;
            goto JUMP;
        }
    }
    elsif ($lvht) {
        $$ilv++;
        ($place,$ini) = split(/<>/,&open_dat($dtedat,'one'));
        &msg("$unm$unt과 $place에 갔습니다");
        &add_record("$unm$unt과 $place에 갔습니다");
        &add_record("$nm$int과 $place에 갔습니다",'other');
        if    ($ini =~ /T/) { $hit = "$fb$ufb" =~ /$ini/ ? 1 : 0 } # 한사람만 가지고 있으면 OK
        else    { $hit = $fb =~ /$ini/ && $ufb =~ /$ini/ ? 1 : 0 } # 두사람 모두 필요
        if ($hit && $ini) {
            &msg("데이트가 상당히 무르익어, 사랑이 깊어졌습니다");
            &add_record("데이트가 무르익어, 사랑이 깊어졌습니다");
            &add_record("데이트가 무르익어, 사랑이 깊어졌습니다",'other');
            $$ilv++; $$ulv += 2;
        }
        $$ilv = $$ilv >= $def_pm ? $def_pm : $$ilv;
        $$ulv = $$ulv >= $def_pm ? $def_pm : $$ulv;
        $shy = 1; $fc++;
    }
    else {
        $$ilv--;
        &msg("$unm$unt과 싸웠습니다");
        &add_record("$unm$unt과 싸웠습니다");
        &add_record("$nm$int과 싸웠습니다",'other');
        $blue = 1; $lp-- if $af + 1 > @ilv; $fc--;
    }
    if ($sx && $$ilv >= $def_pg && $$ulv >= $def_pg && !$pg && $hw eq $uid && ($fb =~ /Y/ || $ufb =~ /Y/)) {
        &msg("$nm$int은 $unm$unt의 아이를 임신했습니다");
        &add_record("$nm$int은 $unm$unt의 아이를 임신했습니다");
        &add_record("$nm$int은 $unm의 아이를 임신했습니다",'other');
        &add_news("$nm$int이 $unm$unt의 아이를 임신했습니다");
        $ulp += $def_bb; $lp += $def_bb;
        $shy  = 1; $fc = $ufc = 4;
        $$ilv = $def_ab;
        $$ulv = $def_ab;
        $unw .= "$nm$int이 $unm의 아이를 임신했습니다<br>";
        $pg   = 1;
    }
    elsif ($$ilv >= $def_mr && $$ulv >= $def_mr && !$hw && !$uhw && $sx ne $usx) {
        if    ($sx  && $fb =~ /Ww/ && $ufb =~ /Wm/) { # 자신이 여성
            &msg("$nm$int은 $unm$unt에게 프로포즈받아 결혼했습니다");
            &add_record("$nm$int은 $unm$unt과 결혼했습니다");
            &add_record("$unm$unt은 $nm$int에게 프로포즈해서 결혼했습니다",'other');
            &add_news("$nm$int과 $unm$unt이 결혼했습니다");
            $hw  = $uid;
            $uhw = $id;
            $shy  = 1; $fc = $ufc = 4;
        }
        elsif (!$sx && $fb =~ /Wm/ && $ufb =~ /Ww/) { # 자신이 남성
            &msg("$nm$int은 $unm$unt에게 프로포즈해서 결혼했습니다");
            &add_record("$nm$int은 $unm$unt과 결혼했습니다");
            &add_record("$unm$unt은 $nm$int에게 프로포즈받아 결혼했습니다",'other');
            &add_news("$nm$int과 $unm$unt이 결혼했습니다");
            $hw  = $uid;
            $uhw = $id;
            $shy  = 1; $fc = $ufc = 4;
        }
    }
    elsif ($$ilv - $$ulv >= $def_ld) {
        &msg("$unm$unt은 $nm$int을 그정도로 사랑하진 않는것 같습니다. $nm$int은 $unm$unt의 앞에서 조용히 떠났습니다.");
        &add_record("$nm$int은 $unm$unt의 앞에서 떠났습니다");
        &add_record("$nm$int은 $unm$unt의 앞에서 떠났습니다",'other');
        &add_news("$nm$int이 $unm$unt의 앞에서 떠났습니다");
        $unw .= "$unm$unt의 사랑이 부족했던 것 같습니다. $nm$int은 $unm$unt의 앞에서 떠났습니다<br>";
        undef $hw  if $hw eq $uid;
        undef $uhw if $uhw eq $id;
        $fc = $lfc = 1; $lp--; $blue = 1;
        splice(@ilv,$no,1);
        delete $ulv{"$id"};
    }
    elsif ($$ilv <= 0) {
        &msg("$unm$unt과 헤어졌습니다");
        &add_record("$unm$unt과 헤어졌습니다");
        &add_record("$nm$int과 헤어졌습니다",'other');
        &add_news("$nm$int은 $unm$unt과 싸우고 헤어졌습니다");
        $unw .= "$nm$int과 싸우고 헤어졌습니다<br>";
        undef $hw  if $hw eq $uid;
        undef $uhw if $uhw eq $id;
        $fc = $lfc = 1; $lp--; $blue = 1;
        splice(@ilv,$no,1);
        delete $ulv{"$id"};
    }

    $fc = $fc < 1 ? 1 : $fc > 4 ? 4 : $fc;
JUMP:
    @lv  = sort grep { $_ } map { join(',',@$_) } @ilv;
    $lv  = join('△',@lv);
    @lv  = sort grep { $_ } map { join(',',@$_) } values %ulv;
    $ulv = join('△',@lv);
    &set_uuser;
}

# Sub Find Lover #
sub find_lover {
    # 자신의 동성애도 체크
    $dice = int(rand($def_bs));
    $ibsc  = $dice > $bs ? 0 : 1;
    # 자신의 적극도 체크
    $dice = int(rand($def_ac + $ac));
    $acc  = $dice < $ac + 1 ? 1 : 0;
    return if !$acc;
    # 자신이 좋아하는 사람 리스트
    %ibl = map  { $_->[0] => [@$_] }
           map  { [split(/,/)] } split(/△/,$bl);
    # 자신의 연인 리스트
    @ilv = sort { $a->[2] <=> $b->[2] }
           map  { [split(/,/)] } split(/△/,$lv);

    # 자신의 바람도 체크
    $iafc  = $af + 1 > @ilv ? 1 : 0;
    return if !$iafc;
    &get_all_users;

    # 모든 주인으로부터 제일 이상형인 상대를 선출
    @lovelines = map  { $_->[0]                              }
                 sort { $b->[3] <=> $a->[3]                  }
                 grep { $id ne $_->[1] && $_->[3] >= $def_lm }
                 grep { $ibsc || $_->[2] ne $sx              }
                 map  { [$_,(split(/<>/))[0,3],
                        &love_match($uv,(split(/<>/))[19])]  } @alllines;

    # 제일 이상형인 상대의 ID를 추출(차였거나 단념한 사람이나 임산부인 경우, 다음 후보)
    foreach (@lovelines) {
        ($uid,$upg) = (split(/<>/))[0,33];
        $love = $ibl{"$uid"}[2];
        if    ($upg) { next }
        elsif ($love =~ /^(bad|giv|luv)$/) { next }
        else { $hit = 1; last }
    }
    $lp++  if !$hit;                            # 후보가 없는 경우, 연인에게 돌아간다.
    return if !$hit;
    return if !&get_uuser($uid);                # 상대의 데이터를 취득

    # 상대의 동성애도 체크
    $dice = int(rand($def_bs));
    $ubsc  = $dice > $ubs ? 0 : 1;
    # 상대가 좋아하는 사람 리스트
    %ubl = map  { $_->[0] => [@$_] }
           map  { [split(/,/)] } split(/△/,$ubl);
    # 상대의 연인 리스트
    @ulv = sort { $a->[3] <=> $b->[3] }
           map  { [split(/,/)] } split(/△/,$ulv);

    # 두사람이 동성인지 아닌지 체크
    $same  = $sx == $usx ? 1 : 0;
    # 다시 두사람이 그런 마음이 있는지 체크
    $homo  = $same && $ibsc && $ubsc ? 1 : 0;
    # 선물 체크
    $dice  = int(rand($def_gp));
    $give  = !$dice && $pr && 1;
    if ($give) {
        $gift = &open_dat($pztdat,'one');
        chomp $gift;
    }

    $umatch = &love_match($uuv,$iv);            # 자신이 상대의 취향인지 체크
    $umatch += $def_pb if $give;                # 선물 보너스
    $dice   = int(rand(100)) + 1;
    if ($dice <= $love * 10) { $pair++        } # 주사위의 수가 러브의 10배보다 낮다
    if ($uaf  >=  $#ulv + 1) { $pair++        } # 상대의 연인의 자리가 비어있다
    if (!$upg)               { $pair++        } # 상대가 임신중은 아니다
    if ($same && !$homo)     { $pair--        } # 동성의 상대에게 그런 마음이 없다
    if ($umatch <= $def_lm)  { $love--        } # 자신이 상대의 취향이 아니다
    elsif ($dice <= $umatch) { $love++;       } # 상대의 호감도보다 다이스가 낮다
    if ($love <= $def_ht)    { $love = 'bad'  } # 일정회수 차이면 영원히 대상에서 제외
    if (!$love)              { $love = 0      }
    $pair = $pair >= 3 ? 1 : 0;                 # 3개의 조건을 모두 더하고 있으면 연인

    &name_title($usx,$sx);

    if ($pair) {                                # 커플 탄생
        push(@ilv,[$uid,$usx,$unm,$love]);      # 자신의 연인 리스트에 추가
        push(@ulv,[$id,$sx,$nm,$love]);         # 상대의 연인 리스트에 추가
        $love = 'luv';                          # 자신이 좋아하는 사람 리스트의 후보에서 제외한다
        $ubl{"$id"} = [$id,$nm,$love];          # 상대가 좋아하는 사람 리스트의 후보에서 제외한다
        &msg("$unm$unt과 연인이 되었습니다");
        &add_record("$unm$unt에게 고백하여 연인이 되었습니다");
        &add_record("$nm$int에게 고백받아 연인이 되었습니다",'other');
        &add_news("$nm$int과 $unm$unt이 연인이 되었습니다");
        $lp  = $def_af - $af;                   # 일정기간 다른 사람을 사랑하지 않게 한다
        $ulp = $def_af - $uaf;                  # 일정기간 다른 사람을 사랑하지 않게 한다
        $ln++; $uln++;                          # 교제한 수를 가산
        $shy = 1; $fc = $ufc = 4;
        $unw .= "$nm$int에게 고백받아 연인이 되었습니다<br>";
    }
    elsif ($love > $def_lo + $ac) { $love = 'giv' }  # 일정회수 상대가 돌아봐 주지 않으면 단념한다

    if ($love eq 'bad') {
        &msg("$unm$unt에게 차였습니다");
        $fc = 1; $rn++; $blue = 1;              # 슬픈 얼굴로 변경, 차인수를 가산
        $lp = 3;                                # 차인 후에는 일정기간 사랑하지 않게 한다
        &add_record("$unm$unt에게 차였습니다");
        &add_record("$nm$int을 거절했습니다",'other');
        &add_news("$nm$int이 $unm$unt에게 차였습니다");
    }
    elsif ($love eq 'giv') {
        &msg("$unm$unt을 포기했습니다");
        $fc = 1; $rn++; $blue = 1;              # 슬픈 얼굴로 변경, 차인수를 가산
        $lp = 3;                                # 차인 후에는 일정기간 사랑하지 않게 한다
        &add_record("$unm$unt을 포기했습니다");
        &add_news("$nm$int이 $unm$unt을 포기했습니다");
    }
    elsif (!$pair) {
        if ($give) {
            &msg("$unm$unt에게 $gift(을/를) 선물했습니다");
            &add_record("$unm$unt에게 $gift(을/를) 선물했습니다");
            &add_record("$nm$int으로부터 $gift(을/를) 선물받았습니다",'other');
           $pr--; $fc++; $shy = 1;
        }
        else {
            &msg("$unm$unt을 사랑하고 있습니다");
            &msg("다만 $unm$unt은 그런 마음이 없는것 같습니다") if $same && !$homo;
            &msg("$unm$unt도 그다지 싫은건 아닌것 같습니다") if $same && $homo;
            &add_record("$nm$int이 당신에게 마음이 있는것 같습니다",'other');
            if ($same && !$homo) { $fc-- } else { $fc++; $shy = 1 }
        }
    }

    $ibl{"$uid"} = [$uid,$unm,$love];           # 자신의 연인 리스트(추가,갱신)

    @bl  = sort grep { $_ } map { join(',',@$_) } values %ibl;
    $bl  = join('△',@bl);
    @lv  = sort grep { $_ } map { join(',',@$_) } @ilv;
    $lv  = join('△',@lv);
    @bl  = sort grep { $_ } map { join(',',@$_) } values %ubl;
    $ubl = join('△',@bl);
    @lv  = sort grep { $_ } map { join(',',@$_) } @ulv;
    $ulv = join('△',@lv);

    $fc = 1 if $fc < 1;
    $fc = 4 if $fc > 4;

    &set_uuser;
}

# Sub Special Action #
sub special_action {
    srand($sec + $min);
    $case = int(rand(10));
    if    ($case == 0) {
        if ($mn > 5)   {
            &msg("5 G를 모금했습니다");
            &add_record("5 G를 모금했습니다");
            $fc++; $mn -= 5;
        }
        else {
            &msg("돈이 없어서 배가 고픕니다");
            $fc--;
        }
    }
    elsif ($case == 1) {
        if ($mn > 10 ) {
            &msg("10 G의 세금을 뜯겼습니다");
            &add_record("10 G의 세금을 뜯겼습니다");
            $fc--; $mn -= 10;
        }
        else {
            &msg("돈이 없어서 자취했습니다");
            $fc--;
        }
    }
    elsif ($case == 2) {
        &msg("5 G를 주웠습니다. 럭키~");
        &add_record("5 G를 주웠습니다");
        $fc++; $mn += 5;
    }
    elsif ($case == 3) {
        &msg("복권으로 10 G 벌었습니다");
        &add_record("복권으로 10 G 벌었습니다");
        $fc++; $mn += 10;
    }
    elsif ($case == 4) { 
        if ($lv) {
            @ilv = map { [split(/,/)] } split(/△/,$lv);
            $no = int(rand(@ilv));
            return if !&get_uuser($ilv[$no][0]);
            $match = (&love_match($uv,$uiv) + &love_match($uuv,$iv)) / 2;
            &msg("점쟁이가 나타났다");
            &msg("「그대와 $unm의 상성은 $match％다!」");
            &add_record("$unm(와/과)의 상성은 $match％라고 점쟁이가 말했다");
        }
    }
    elsif ($case == 5) {
        if ($pr) {
            &msg("도둑에게 선물을 도둑맞았다");
            &add_record("도둑에게 선물을 도둑맞았다");
            $fc--; $pr--;
        }
        elsif ($pr < $def_pr && $pnm) {
            &msg("$pnm(이/가) 선물이 될만한 것을 주워왔습니다");
            &add_record("$pnm(이/가) 선물이 될만한 것을 주워왔습니다");
            $fc++; $pr++;
        }
        elsif ($pr < $def_pr) {
            &msg("추첨으로 선물이 당첨되었습니다");
            &add_record("선물이 당첨되었습니다");
            $fc++; $pr++;
        }
        else { &msg("오늘은 외톨이였습니다‥") }
    }
    elsif ($case == 6) {
        if ($pfd) {
            &msg("어느사이엔가 애완동물의 먹이가 상했습니다");
            &add_record("애완동물의 먹이가 상했습니다");
            $pfd--;
        }
        elsif ($pfd < $def_pf) {
            &msg("서랍에서 애완동물의 먹이를 찾았습니다");
            &add_record("애완동물의 먹이를 찾았습니다");
            $pfd++;
        }
        else { &msg("사람이 그리워서 눈물을 흘렸습니다‥") }
    }
    else { &msg("멍하게 있었습니다") }
    $fc = $fc < 1 ? 1 : $fc > 4 ? 4 : $fc;
}

# Sub Pet Action #
sub pet_action {
    return if !$pim;
    $pet = $pnm ? $pnm : '애완동물';
    local($age) = &get_age($ptm);
    while ($age >= $def_pe && $pfd) {
        $age -= $def_pe;
        $ptm += $def_pe * 86400;
        $pfd--;
        &get_date($ptm);
        &add_record("$pet(이/가) 먹이를 먹었습니다");
    }
    if ($age >= $def_pl) {
        &get_date($ptm + ($def_pl * 86400));
        &msg("$pet(이/가) 굶주림에 죽었습니다");
        &add_record("$pet(이/가) 아사했습니다");
        $pnm = $pim = $ptm = '';
        $fc = $blue = 1;
        return;
    }
    &get_date(time);
    $case = int(rand(5));
    $case = -1 if $age >= $def_pe;
    srand($sec); # 일시적인 안심
    if    ($case < 0)  { # 배가 꺼졌다
        &pet_msg("배고파서 죽을것 같다");
    }
    elsif ($case == 0 && !$dead) { # 놀러간다
        &get_all_users;
        $uid  = (split(/<>/,$alllines[int(rand(@alllines))]))[0];
        if ($uid eq $id) {
            &pet_msg("집에서 데굴데굴 굴렀다");
        }
        else {
            &get_uuser($uid);
            &name_title($usx,$sx);
            &pet_msg("$unm$unt의 집에 놀러갔다");
            ($upnm,$upim,$upfd,$uptm,$updt) = split(/,/,$upt);
            if ($upim) {
                $upet = $upnm ? $upnm : '애완동물';
                $dice = int(rand(@IPC));
                $imsg = "．$upet$IPC[$dice]";
                $umsg = "．$upet는 $nm$int의 $pet$UPC[$dice]";
                &pet_msg($imsg);
                $imsg .= '그렇습니다';
            }
            &add_record("$pet(이/가) $unm$unt의 집에 놀러 갔습니다 $imsg");
            &add_record("$nm$int의 $pet(이/가) 놀러 왔습니다 $umsg",'other');
            &set_uuser;
        }
    }
    elsif ($case == 1) { # 무언가 주워온다
        $gift = &open_dat($pztdat,'one');
        chomp $gift;
        &pet_msg("$gift(을/를) 주웠다");
    }
    elsif ($case == 2) { # 사육주 관찰
        if    ($blue)    { &pet_msg("$nm(이/가) 풀죽어 있다")     }
        elsif ($shy)     { &pet_msg("$nm(이/가) 기뻐하고 있다")   }
        elsif ($fc == 0) { &pet_msg("$nm의 상태가 안좋아 보인다") }
        elsif ($fc == 1) { &pet_msg("$nm에게 얻어맞았다")         }
        elsif ($fc == 2) { &pet_msg("$nm에게 무시 당했다")        }
        elsif ($fc == 3) { &pet_msg("$nm(이/가) 쓰다듬어 줬다")   }
        elsif ($fc == 4) { &pet_msg("$nm(이/가) 놀아주었다")      }
        else             { &pet_msg("$nm(과/와) 놀아주었다")      }
    }
    elsif ($case >= 3) { # 그 외
        $diary = &open_dat($petdat,'one');
        chomp $diary;
        $diary =~ s/○○/$nm/g;
        &pet_msg("$diary");
    }
}

# Sub Love Potion #
sub love_potion {
    @ibl  = map { [split(/,/)] } split(/△/,$bl);
    %dlv  = map { $_->[0] => [@$_] }
            map { [split(/,/)] } split(/△/,$lv);
    foreach (0 .. $#ibl) {
        if ($ibl[$_][2] =~ /^(bad|giv|luv)$/ && !$dlv{$ibl[$_][0]}) { push(@bbl,$ibl[$_]) }
        else { push(@gbl,$ibl[$_]) }
    }
    if (@bbl) {
        srand(time);
        $dice = int(rand(@bbl));
        &msg("$inm에 의해 $bbl[$dice][1]을 향한 사랑이 다시 불타올랐다");
        splice(@bbl,$dice,1);
        @ibl  = (@bbl,@gbl);
        @ibl  = sort grep { $_ } map { join(',',@$_) } @ibl;
        $bl   = join('△',@ibl);
        $fc   = 5;
    }
    else {
        &msg("$inm은 지금의 $nm에게는 효과가 없었습니다. $ipc G는 헛돈이였나보다‥");
    }
    undef @ibl,%dlv;
}
1;
