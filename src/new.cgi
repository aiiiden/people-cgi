use utf8;
use Encode;
binmode(STDOUT, ":utf8");   # 표준 출력은 UTF-8로 설정
binmode(STDIN, ":utf8");    # 표준 입력도 UTF-8로 설정


# ##################################################################
# PeoPle(new.cgi)
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

# Sub New Regist #
sub new_regist {
    &header('java');
    &first_box('up');
    &second_box('up','form');
    &title;
    &label('신규등록');
    &info_button;
    &return_button('','br','link');

    print qq|이름（경칭은 자동으로 붙습니다）<br>\n|;
    print qq|<input type=text name=nm class=text size=$stx_wth><br>\n|;
    print qq|패스워드<br>\n|;
    print qq|<input type=password name=ps class=text size=$stx_wth><br>\n|;
    print qq|메일 (임의)<br>\n|;
    print qq|<input type=text name=ml class=text size=$ltx_wth><br>\n|;
    print qq|홈페이지 주소 (임의)<br>\n|;
    print qq|<input type=text name=ul class=text size=$ltx_wth><br>\n|;
    print qq|성별 |;
    print qq|$man_img<input type=radio name=sx value="0" checked>\n|;
    print qq|$wmn_img<input type=radio name=sx value="1">\n|;
    print qq|<input type=hidden name=mode value="set_regist">\n|;

    &submit_button;
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub Set Regist #
sub set_regist {
    if ($ENV{'REQUEST_METHOD'} ne "POST") { &error('부정확한 에러입니다') }
    &error("이름을 입력해 주세요")                if !$F{'nm'};
    &error("이름은 반각 $def_nb문자까지")         if length $F{'nm'} > $def_nb;
    &error("반각 코론「:」은 사용할 수 없습니다") if  $F{'nm'} =~ /:/;
    &error("삼각형「△」은 사용할 수 없습니다")   if  $F{'nm'} =~ /△/;
    &error("패스워드를 입력해 주세요")            if !$F{'ps'};
    &error("메일의 입력이 부정확 합니다")         if  $F{'ml'} && $F{'ml'} !~ /(.*)\@(.*)\.(.*)/;

    &get_all_users;
    $def_mp && @alllines >= $def_mp && &error("현제, 플레이어 수가 $def_mp명을 넘었기 때문에 신규등록은 받지 않습니다.");
    &get_host;

    ($namecheck) = grep { $_->[0] eq $F{'nm'} }
                   map  { [(split(/<>/))[1]] } @alllines;
    ($mailcheck) = grep { $_->[0] && $_->[0] eq $F{'ml'} }
                   map  { [(split(/<>/))[4]] } @alllines if $F{'ml'};
    ($urlcheck)  = grep { $_->[0] && $_->[0] eq $F{'ul'} }
                   map  { [(split(/<>/))[5]] } @alllines if $F{'ul'};
    ($ipcheck)   = grep { &ip_check($ht,$_->[0]) }
                   map  { [(split(/<>/))[25]] } @alllines if $def_ip;
    ($idcheck)   = map  { $_->[0] }
                   sort { $b->[0] <=> $a->[0] }
                   map  { [(split(/<>/))[0]] } @alllines;

    if ($F{'ps'} =~ s/^$def_ei//) { undef $ipcheck }
    if ($namecheck) { &error("그 이름은 이미 사용중 입니다") }
    if ($mailcheck) { &error("그 메일은 이미 사용중 입니다") }
    if ($urlcheck)  { &error("그 홈페이지 주소는 이미 사용중 입니다") }
    if ($ipcheck)   { &error("같은 IP를 사용하는 플레이어가 이미 가입되어 있어서 신규등록을 할 수 없습니다") }

    $id = sprintf("%06d",$idcheck + 1);
    $nm = $F{'nm'};  $mn = $def_fm;
    $ps = &set_crypt($F{'ps'});
    $sx = $F{'sx'};  $ag = time;
    $ml = $F{'ml'};  $lp = 1;
    $ul = $F{'ul'};  $fc = 2;
    $ln = $rn = $fp = 0;
    $nw = $def_nw;
    $t1 = time - 86400;
    $t2 = time;
    &get_agent;
    @ilines = ("$hismsg");
    &set_iuser;
    chmod(0666,"$usrdir\/$id\.dat");

    $F{'id'} = $id;
    &set_cookie;

    &header('java');
    &first_box('up');
    &second_box('up','form');
    &title;
    &label('등록완료');
    &info_button;

    print qq|등록을 완료했습니다<br>\n|;
    print qq|ID는 $id입니다.<br>\n|;
    print qq|패스워드는 $F{'ps'}입니다.<br><br>\n|;
    print qq|ID와 패스워드는 메모해 두세요.<br>\n|;

    &submit_button;
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub Set Virtue #
sub set_virtue {
    &get_iuser($F{'id'});
    &error("부정확한 에러입니다") if $iv || $uv;
    # 본인설정
    foreach (0 .. $def_tv - 1) {
        &error("$VT[$_](자신)의 수치가 입력되어 있지 않습니다") if $F{"i$_"} eq '';
        &error("$VT[$_](자신)의 수치가 잘못 입력 되었습니다(1∼8)") if $F{"i$_"} =~ /[^1-8]/;
        &error("순위(자신)가 중복되었습니다") if $icheck[$F{"i$_"}];
        $icheck[$F{"i$_"}] = 'on';
        $iv .= $F{"i$_"};
        if ($F{"i$_"} <= 4) {
            $bs += $BS[$_]; # 동성애설정
            $ac += $AC[$_]; # 적극도설정
            $af += $AF[$_]; # 바람도설정
        }
    }
    # 상대설정
    foreach (0 .. $def_tv - 1) {
        &error("$VT[$_](상대)의 수치가 입력되어 있지 않습니다") if $F{"u$_"} eq '';
        &error("$VT[$_](상대)의 수치가 잘못 입력 되었습니다(1∼8)") if $F{"u$_"} =~ /[^1-8]/;
        &error("순위(상대)가 중복되었습니다") if $ucheck[$F{"u$_"}];
        $ucheck[$F{"u$_"}] = 'on';
        $uv .= $F{"u$_"};
    }
    &play_view;
}

# Sub New Job #
sub new_job {
    &get_iuser($F{'id'});
    $fl='NJB'; &set_iuser;
    &header;
    &first_box('up');
    &second_box('up','form');
    &title;
    &label('전직');
    @joblines = &open_dat($jobdat);
    print qq|적업을 선택하여 주세요. 전직하면 $JL[0]부터 시작하게 됩니다.<br>\n|;
    print qq|<select name=job class=text>\n|;
    foreach (0 .. $#joblines) {
        ($jsx,$jnm) = split(/<>/,$joblines[$_]);
        next if $jsx != $sx && $jsx != 2;
        print qq|<option value="$_">$jnm\n|;
    }
    undef @joblines;
    print qq|</select>\n|;
    print qq|<input type=hidden name=mode value="set_new_job">\n|;
    &id_ps;
    &submit_button;
    &return_button("play_view&id=$F{'id'}&ps=$F{'ps'}",'','button');
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub Set New Job #
sub set_new_job {
    &get_iuser($F{'id'});
    if ($fl ne 'NJB') { &play_view; return }
    $fl = '';
    $jb = join(',',(split(/<>/,(&open_dat($jobdat))[$F{'job'}]))[1,2,3,4],0,time);
    &msg("새로운 일에 조금 불안");
    $fc-- if $fc > 1;
    &play_view;
}

# Sub Pet Name #
sub pet_name {
    &header;
    &first_box('up');
    &second_box('up','form');
    &title;
    &label('애완동물의 이름');
    print qq|애완동물에게 이름을 붙여 주세요<br>\n|;
    print qq|<input type=text name=pnm class=text size=$stx_wth>\n|;
    print qq|<input type=hidden name=mode value="set_pet_name">\n|;
    &id_ps;
    &submit_button;
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub Set Pet Name #
sub set_pet_name {
    &get_iuser($F{'id'});
    &error("부정확한 에러입니다")                 if $pnm;
    &error("이름을 입력해 주세요")                if !$F{'pnm'};
    &error("이름은 반각 $def_nb문자까지")         if length $F{'pnm'} > $def_pn;
    &error("반각 코론「:」은 사용할 수 없습니다") if  $F{'pnm'} =~ /:/;
    &error("삼각형「△」은 사용할 수 없습니다")   if  $F{'pnm'} =~ /△/;
    $pnm = $F{'pnm'};
    &play_view;
}

# Sub Info Virtue #
sub info_virtue {
    &header;
    &first_box('up','smallwindow');
    &second_box('up','form');
    &title;
    &label('덕목의 설명');
    print &open_dat($vtddat);
    &second_box('down');
    &first_box('down');
    &footer('nocopyright');
}

# Sub Select Icon #
sub select_icon {
    &get_iuser($F{'id'});
    @icn_nm = $sx ? @icn_wn : @icn_mn;
    @icn_fl = $sx ? @icn_wf : @icn_mf;
    &header;
    &first_box('up');
    &second_box('up','form');
    &title;
    &label('아이콘의 선택');
    print qq|아이콘을 선택해 주세요<br>\n|;
    print qq|<a href="$icn_lt" target=_blank>아이콘 일람</a><br>| if $def_lt;
    print qq|<select name=ci class=text>\n|;
    foreach (0 .. $#icn_nm) {
        print qq|<option value="$icn_fl[$_]">$icn_nm[$_]\n|;
    }
    print qq|</select>\n|;
    print qq|<input type=hidden name=mode value="set_icon">\n|;
    &id_ps;
    &submit_button;
    &return_button("play_view&id=$F{'id'}&ps=$F{'ps'}",'','button');
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub Set Icon #
sub set_icon {
    &get_iuser($F{'id'});
    $ci = $F{'ci'};
    &play_view;
}

1;
