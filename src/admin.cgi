#!/usr/bin/perl

use utf8;  # Perl 내부에서 UTF-8 지원
binmode(STDOUT, ":encoding(EUC-KR)");  # 출력 인코딩을 EUC-KR로 설정

print "Content-type: text/html; charset=EUC-KR\n\n";

# ↑서버에 맞게 변경해 주세요.
# 보통 (#!/usr/local/bin/perl) 또는 (#!/usr/bin/perl)

# ##################################################################
# PeoPle For Adminster
    $ver = '1.3';
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

# ############################ 설정시작 ############################

# ↓유저 데이터를 보관할 디렉토리명(보안을 위해 반드시 변경해주세요)
# 변경한 이름과 같은 이름의 디렉토리를 people.cgi와 같은 장소에 작성
# 퍼미션은 777 또는 707로 합니다.

$usrdir  = '/var/www/html/user';

# ↓PeoPle에서 사용하는 모든 그림을 보관하는 디렉토리 입니다.
# 절대주소(http://로 시작되는 주소)도 상대주소도 상관없습니다.
# 초기값은 people.cgi와 같은 장소에 배치 하도록 되있습니다.
# 프로바이더(서버)에 따라서는 cgi-bin아래에 그림 디렉토리를
# 두는 것을 금지하고 있는 경우가 있습니다. 그런 경우에는
# cgi-bin보다 위쪽에 그림 디렉토리를 배치하고 주소를 변경해 주세요.

$img     = '/img';       # 주의：마지막에 슬레쉬(/)를 붙이지 말아주세요.

$hom_url = 'http://';     # 돌아올 홈의 URL
$hom_tgt = '_self';       # 돌아올 홈의 타겟
$hom_lbl = '홈';          # 돌아올 홈의 라벨
$def_ho  = 1;             # 돌아올 홈의 버튼을 표시한다(yes = 1,no = 0)

# ---------- LOCK
$lockkey = 1;             # 파일의 락(rmdir = 1,symlink = 2,no = 0)
                          # symlink가 잘되지 않는 경우엔 rmdir을 사용해 주세요.

# ---------- COOKIE
$cookname = 'PPA';        # 쿠키명(변경추천,people.cgi의 것과는 다른 이름으로 해주세요.)

$adps     = '1234';       # 관리자 패스워드

$title    = 'PeoPle For Administer';     # 타이틀명(브라우저 위쪽에 표시)
$body     = '<body bgcolor=#FFFFFF text=#000000>';    # 보디 태그

$fnt_sze  = '8pt';        # 폰트 사이즈

$mtb_wth  = 350;          # 메인테이블의 폭
$tbl_bgc  = '#FFDFFF';    # 테이블의 배경색
$tbl_lnc  = '#FF66FF';    # 태이블의 라인의 색

$nlc_clr  = '#CC00CC';    # 링크색(방문전)
$vlc_clr  = '#FF0000';    # 링크색(방문후)
$alc_clr  = '#990099';    # 링크색(방문중)

$def_ti   = 1;            # 타이틀 화상을 표시한다(yes = 1,no = 0)
$ttl_img  = 'title.gif';  # 타이틀 화상(파일명만)
$ttl_wth  = 100;          # 타이틀 화상 가로폭
$ttl_hgt  = 25;           # 타이틀 화상 세로폭

$sub_lbl  = 'OK';         # 결정 버튼의 라벨
$bak_lbl  = '뒤로';       # 돌아올 버튼의 라벨
$but_sze  = 8;            # 버튼의 문자 사이즈
$stx_wth  = 20;           # 텍스트 입력란의 폭(소)
$ltx_wth  = 35;           # 텍스트 입력란의 폭(대)
$txb_sze  = 10;           # 텍스트 입력란의 문자 사이즈
$txb_clr  = '#FFCCFF';    # 텍스트 입력란과 버튼의 배경색

$def_rb   = 0;            # 돌아올 버튼을 모두 링크버튼으로 한다(yes=1,no=0)
                          # 바로 메뉴로 돌아오고 싶은 경우에는 yes로 해주세요.

# ############################ 설정종료 ############################

# ############################ 응용설정 ############################
# 이하의 항목은 보통 변경 불필요

# ---------- FILE PASS
$cgiurl  = './admin.cgi';  # admin.cgi의 주소(보통 변경 불필요) 755(705)
$jobdat  = '/var/www/html/dat/job.dat';    # job.dat
$itmdat  = '/var/www/html/dat/itm.dat';    # itm.dat
$chddat  = '/var/www/html/dat/chd.dat';    # chd.dat
$elsdat  = '/var/www/html/dat/els.dat';    # els.dat
$dtedat  = '/var/www/html/dat/dte.dat';    # dte.dat
$pztdat  = '/var/www/html/dat/pzt.dat';    # pzt.dat
$petdat  = '/var/www/html/dat/pet.dat';    # pet.dat
$htpdat  = '/var/www/html/dat/htp.dat';    # htp.dat
$vtidat  = '/var/www/html/dat/vti.dat';    # vti.dat
$vtddat  = '/var/www/html/dat/vtd.dat';    # vtd.dat

$lockfile= './ppllock';    # 락파일명

# ---------- METHOD
$method  = 'POST';         # POST or GET *POST추천

$hrt_img = "<img src=\"$img/heart.gif\">";         # 하트의 화상
$mel_img = "<img src=\"$img/mail.gif\" border=0>"; # 메일의 화상
$url_img = "<img src=\"$img/url.gif\" border=0>";  # 사이트주소의 화상

# ############################ 설정종료 ############################

# ####################### 메인 프로그램 개시 #######################
&error("유저 디렉토리명을 변경해주세요[$cgiurl의29행]") if $usrdir eq 'userdata';
&error("관리 패스워드를 변경해주세요[$cgiurl의52행]") if $adps eq '0000';
&decode;
if ($F{'id'} =~ /\W/) { &error('부정확한 입력입니다') }

if (!$F{'mode'}) { &start_view     }
else             { &{$F{'mode'}}   }
&unlock;
exit;
# ####################### 메인 프로그램 종료 #######################

# ######################### 서브 루틴 개시 #########################

# Sub Start View #
sub start_view {
    &header;
    &first_box('up','150');
    &second_box('up','form');
    &title;

    &get_cookie;
    print qq|<center>\n|;
    print qq|관리자 패스워드<br>\n|;
    print qq|<input type=password name=ps class=text size=$stx_wth value="$c_ps">\n|;
    print qq|<input type=hidden name=mode value="menu">\n|;
    print qq|</center>\n|;
    &submit_button;
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub Menu #
sub menu {
    &error("패스워드 부정확") if $F{'ps'} ne $adps;
    &set_cookie if $F{"ps"}; 
    &header;
    &first_box('up','170');
    &second_box('up','form');
    &title;

    &label('메뉴');
    print qq|<input type=radio name=mode value="item_before" checked>아이템<br>\n|;
    print qq|<input type=radio name=mode value="job_before">직업<br>\n|;
    print qq|<input type=radio name=mode value="child_before">아이<br>\n|;
    print qq|<input type=radio name=mode value="present_before">선물<br>\n|;
    print qq|<input type=radio name=mode value="date_before">데이트<br>\n|;
    print qq|<input type=radio name=mode value="pet_before">애완동물일기\n|;
    print qq|<hr class=text>\n|;
    print qq|<input type=radio name=mode value="iplay_before">설명서<br>\n|;
    print qq|<input type=radio name=mode value="ichar_before">캐릭터 설정의 설명<br>\n|;
    print qq|<input type=radio name=mode value="ivirt_before">덕목의 설명<br>\n|;
    print qq|<hr class=text>\n|;
    print qq|<input type=radio name=mode value="player_data">플레이어 데이터\n|;
    &ps;

    &submit_button;
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub Item Before #
sub item_before {
    &error("패스워드 부정확") if $F{'ps'} ne $adps;
    &header;
    &first_box('up','170');
    &second_box('up','form');
    &title;

    &label('아이템');
    @itmlines = &open_dat($itmdat);
    print qq|<table align=center width=100%>\n|;
    print qq|<tr><td colspan=5>|.
          qq|신규등록 - 가장 아래의 공란에 추가합니다.<br>|.
          qq|삭제 - 아이템명을 공백으로 해주세요.<br><br>|.
          qq|아이템명／가격／그림파일／종류1／종류2／성별<br>|.
          qq|성별：남성용=0, 여성용=1<br>|.
          qq|데이트용 아이템：데이트용으로 사용하는 아이템입니다.<br>|.
          qq|S - 두사람 모두 그 아이템을 가지고 있으면 OK<br>|.
          qq|T - 데이트하는 두사람 중 한사람이 가지고 있으면 OK<br>|.
          qq|약자가 있는 데이트 장소의 경우 같은 약자의 아이템을 가지고 있으면 데이트의 효과는 높아지고, 두사람의 사랑이 깊어집니다.<br>|.
          qq|<pre>A - 선물<br>|.
          qq|C - 메일 필수 아이템<br>|.
          qq|  Ca - 아이템1, Cb - 아이템2<br>|.
          qq|E - 애완동물<br>|.
          qq|F - 애완동물의 먹이<br>|.
          qq|L - 사랑의 미약<br>|.
          qq|S - 데이트용 아이템(두사람 모두 필요)<br>|.
          qq|T - 데이트용 아이템(한사람만 가지고 있으면 OK)<br>|.
          qq|W - 결혼필수 아이템<br>|.
          qq|  Wm - 남성전용，Ww - 여성전용<br>|.
          qq|Y - 임신필수 아이템(한사람만 가지고 있으면 OK)<br>|.
          qq|Z - 기타</pre>|.
          qq|주의1：종류1, 종류2를 조합해서 약자로 사용합니다.|.
          qq|애완동물 먹이의 경우, 종류2는 갯수로 사용합니다.<br>|.
          qq|주의2：성별을 지정하면 그 성별의 사람밖에 살 수 없게 됩니다.<br>|.
          qq|주의3：아이템은 종류순서(알파벳순서), 가격이 싼 순서대로 정렬되고 고쳐집니다.|.
          qq|</td></tr>\n|;
    foreach (0 .. $#itmlines + 1) {
        ($inm,$ipc,$iim,$iin,$ipt,$isx) = split(/<>/,$itmlines[$_]);
        print qq|<tr>\n|;
        print qq|<td><input type=text name="inm$_" value="$inm" class=text></td>\n|;
        print qq|<td><input type=text name="ipc$_" value="$ipc" class=text size=3></td>\n|;
        print qq|<td><input type=text name="iim$_" value="$iim" class=text></td>\n|;
        print qq|<td><input type=text name="iin$_" value="$iin" class=text size=2></td>\n|;
        print qq|<td><input type=text name="ipt$_" value="$ipt" class=text size=2></td>\n|;
        print qq|<td><input type=text name="isx$_" value="$isx" class=text size=2></td>\n|;
        print qq|</tr>\n|;
    }
    print qq|</table>\n|;
    print qq|<input type=hidden name=mode value="item_after">\n|;
    &ps;

    &submit_button;
    &return_button("menu&ps=$F{'ps'}",'','button');
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub Item After #
sub item_after {
    @itmlines = &open_dat($itmdat);
    foreach (0 .. $#itmlines + 1) {
        ($inm,$ipc,$iim,$iin,$ipt) = split(/<>/,$itmlines[$_]);
        $name = $F{"inm$_"};
        if (!$F{"inm$_"}) { next }

        if ($F{"ipc$_"} eq '') { &error("$name의 가격이 설정되지 않았습니다") }
        if ($F{"iim$_"} eq '') { &error("$name의 그림파일이 설정되지 않았습니다") }
        if ($F{"iin$_"} eq '') { &error("$name의 종류가 설정되지 않았습니다") }

        if ($F{"ipc$_"} =~ /[^0-9]/)    { &error("$name의 가격이 부정확 합니다") }
        if ($F{"iin$_"} =~ /[^a-zA-Z]/) { &error("$name의 종류가 부정확 합니다") }
        if ($F{"isx$_"} && $F{"isx$_"} =~ /[^1-2]/) { &error("$name의 성별이 부정확 합니다") }

        if ($F{"inm$_"} ne $inm) { $inm = $F{"inm$_"} }
        if ($F{"ipc$_"} ne $ipc) { $ipc = $F{"ipc$_"} }
        if ($F{"iim$_"} ne $iim) { $iim = $F{"iim$_"} }
        if ($F{"iin$_"} ne $iin) { $iin = $F{"iin$_"} }
        if ($F{"ipt$_"} ne $ipt) { $ipt = $F{"ipt$_"} }
        if ($F{"isx$_"} ne $isx) { $isx = $F{"isx$_"} }
        push (@newlines,join('<>',$inm,$ipc,$iim,$iin,$ipt,$isx,"\n"));
    }
    @newlines = map  { $_->[0] }
                sort { $a->[4] cmp $b->[4] || $a->[2] <=> $b->[2] || $a->[5] cmp $b->[5] || $a->[1] cmp $b->[1] }
                map  { [$_,split(/<>/)] } @newlines;
    &write_dat($itmdat,@newlines);
    &item_before;
}

# Sub Job Before #
sub job_before {
    &error("패스워드 부정확") if $F{'ps'} ne $adps;
    &header;
    &first_box('up','170');
    &second_box('up','form');
    &title;

    &label('직업');
    @joblines = &open_dat($jobdat);
    print qq|<table align=center width=100%>\n|;
    print qq|<tr><td colspan=5>|.
          qq|신규등록 - 가장 아래의 공란에 추가합니다.<br>|.
          qq|삭제 - 직업명을 공백으로 해주세요.<br><br>|.
          qq|성별／직업명／기본급／승진할 확률(%)／승진후 기본급에 가산되는 액수<br><br>|.
          qq|성별에 대해<br>|.
          qq|0 - 남성만<br>|.
          qq|1 - 여성만<br>|.
          qq|2 - 남녀모두OK|.
          qq|</td></tr>\n|;
    foreach (0 .. $#joblines + 1) {
        ($jsx,$jnm,$jss,$jpc,$jbn) = split(/<>/,$joblines[$_]);
        print qq|<tr>\n|;
        print qq|<td><input type=text name="jsx$_" value="$jsx" class=text size=2></td>\n|;
        print qq|<td><input type=text name="jnm$_" value="$jnm" class=text></td>\n|;
        print qq|<td><input type=text name="jss$_" value="$jss" class=text size=3></td>\n|;
        print qq|<td><input type=text name="jpc$_" value="$jpc" class=text size=3></td>\n|;
        print qq|<td><input type=text name="jbn$_" value="$jbn" class=text size=2></td>\n|;
        print qq|</tr>\n|;
    }
    print qq|</table>\n|;
    print qq|<input type=hidden name=mode value="job_after">\n|;
    &ps;

    &submit_button;
    &return_button("menu&ps=$F{'ps'}",'','button');
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub Job After #
sub job_after {
    @joblines = &open_dat($jobdat);
    foreach (0 .. $#joblines + 1) {
        ($jsx,$jnm,$jss,$jpc,$jbn) = split(/<>/,$joblines[$_]);
        $name = $F{"jnm$_"};
        if (!$F{"jnm$_"}) { next }

        if ($F{"jsx$_"} eq '') { &error("$name의 성별이 설정되지 않았습니다") }
        if ($F{"jss$_"} eq '') { &error("$name의 기본급이 설정되지 않았습니다") }
        if ($F{"jpc$_"} eq '') { &error("$name의 승진할 확률이 설정되지 않았습니다") }
        if ($F{"jbn$_"} eq '') { &error("$name의 가산액이 설정되지 않았습니다") }

        if ($F{"jsx$_"} =~ /[^0-2]/)  { &error("$name의 성별이 부정확 합니다") }
        if ($F{"jss$_"} =~ /[^0-9]/)  { &error("$name의 기본급이 부정확 합니다") }
        if ($F{"jpc$_"} =~ /[^0-9.]/) { &error("$name의 승진확률이 부정확 합니다") }
        if ($F{"jbn$_"} =~ /[^0-9]/)  { &error("$name의 가산액이 부정확 합니다") }

        if ($F{"jsx$_"} ne $jsx) { $jsx = $F{"jsx$_"} }
        if ($F{"jnm$_"} ne $jnm) { $jnm = $F{"jnm$_"} }
        if ($F{"jss$_"} ne $jss) { $jss = $F{"jss$_"} }
        if ($F{"jpc$_"} ne $jpc) { $jpc = $F{"jpc$_"} }
        if ($F{"jbn$_"} ne $jbn) { $jbn = $F{"jbn$_"} }
        push (@newlines,join('<>',$jsx,$jnm,$jss,$jpc,$jbn,"\n"));
    }
    &write_dat($jobdat,@newlines);
    &job_before;
}

# Sub Child Before #
sub child_before {
    &error("패스워드 부정확") if $F{'ps'} ne $adps;
    &header;
    &first_box('up','170');
    &second_box('up','form');
    &title;

    &label('아이');
    @chdlines = &open_dat($chddat);
    print qq|추가 - 임의의 이름을 추가합니다.<br>|.
          qq|삭제 - 각 이름을 삭제해 주세요.<br><br>|.
          qq|주의：리스트는 ㄱㄴㄷㄹ순으로 정렬됩니다.<br>|;
    print qq|<textarea rows=15 cols=30 name=child class=text>\n|;
    foreach (@chdlines) { print qq|$_| }
    print qq|</textarea><br>\n|;
    print qq|<input type=hidden name=mode value="child_after">\n|;
    &ps;

    &submit_button;
    &return_button("menu&ps=$F{'ps'}",'','button');
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub Child After #
sub child_after {
    $F{'child'} =~ s/&lt;/</g;
    $F{'child'} =~ s/&gt;/>/g;
    @children = sort split(/<br>/,$F{'child'});
    foreach (@children) { push(@chdlines,"$_\n") if $_ }
    &write_dat($chddat,@chdlines);
    &child_before;
}

# Sub Present Before #
sub present_before {
    &error("패스워드 부정확") if $F{'ps'} ne $adps;
    &header;
    &first_box('up','170');
    &second_box('up','form');
    &title;

    &label('선물');
    @pztlines = &open_dat($pztdat);
    print qq|추가 - 임의의 이름을 추가합니다.<br>|.
          qq|삭제 - 각 이름을 삭제해 주세요.<br>|;
    print qq|<textarea rows=15 cols=30 name=present class=text>\n|;
    foreach (@pztlines) { print qq|$_| }
    print qq|</textarea><br>\n|;
    print qq|<input type=hidden name=mode value="present_after">\n|;
    &ps;

    &submit_button;
    &return_button("menu&ps=$F{'ps'}",'','button');
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub Present After #
sub present_after {
    $F{'present'} =~ s/&lt;/</g;
    $F{'present'} =~ s/&gt;/>/g;
    @present = split(/<br>/,$F{'present'});
    foreach (@present) { push(@pztlines,"$_\n") if $_ }
    &write_dat($pztdat,@pztlines);
    &present_before;
}

# Sub Date Before #
sub date_before {
    &error("패스워드 부정확") if $F{'ps'} ne $adps;
    &header;
    &first_box('up','170');
    &second_box('up','form');
    &title;

    &label('데이트');
    @dtelines = &open_dat($dtedat);
    print qq|아이템명／약자<br>|.
          qq|추가 - 임의의 데이터를 추가합니다.<br>|.
          qq|삭제 - 각 데이터를 삭제해 주세요.<br>|.
          qq|약자 - 약자가 있는것은 각각 같은 약자의 아이템에 대응하고 있습니다. 대응하는 아이템을 가지고 있는경우, 데이트의 효과는 높아지고, 사랑이 깊어집니다.<br><br>|.
          qq|주의 - 게임중은「××와 ○○에 갔습니다」라고 표시됩니다.<br>|;
    print qq|<textarea rows=15 cols=30 name=date class=text>\n|;
    foreach (@dtelines) { print qq|$_| }
    print qq|</textarea><br>\n|;
    print qq|<input type=hidden name=mode value="date_after">\n|;
    &ps;

    &submit_button;
    &return_button("menu&ps=$F{'ps'}",'','button');
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub Date After #
sub date_after {
    $F{'date'} =~ s/&lt;/</g;
    $F{'date'} =~ s/&gt;/>/g;
    @date = split(/<br>/,$F{'date'});
    foreach (@date) { push(@dtelines,"$_\n") if $_ }
    &write_dat($dtedat,@dtelines);
    &date_before;
}

# Sub Pet Before #
sub pet_before {
    &error("패스워드 부정확") if $F{'ps'} ne $adps;
    &header;
    &first_box('up','170');
    &second_box('up','form');
    &title;

    &label('애완동물일기');
    @petlines = &open_dat($petdat);
    print qq|추가 - 임의의 문장을 추가합니다.<br>|.
          qq|삭제 - 각 문장을 삭제해주세요.<br>|.
          qq|○○을 입력하면 그곳에 주인의 이름이 들어갑니다.<br>|;
    print qq|<textarea rows=15 cols=30 name=pet class=text>\n|;
    foreach (@petlines) { print qq|$_| }
    print qq|</textarea><br>\n|;
    print qq|<input type=hidden name=mode value="pet_after">\n|;
    &ps;

    &submit_button;
    &return_button("menu&ps=$F{'ps'}",'','button');
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub Pet After #
sub pet_after {
    $F{'pet'} =~ s/&lt;/</g;
    $F{'pet'} =~ s/&gt;/>/g;
    @pet = split(/<br>/,$F{'pet'});
    foreach (@pet) { push(@petlines,"$_\n") if $_ }
    &write_dat($petdat,@petlines);
    &pet_before;
}

# Sub Information Play Before #
sub iplay_before {
    &error("패스워드 부정확") if $F{'ps'} ne $adps;
    &header;
    &first_box('up','170');
    &second_box('up','form');
    &title;

    &label('설명서');
    ($howtoplay) = &open_dat($htpdat);
    $howtoplay =~ s/<br>/\n/g;
    print qq|설명서의 설명을 편집합니다.<br>|;
    print qq|<textarea rows=15 cols=50 name=play class=text>\n|;
    print $howtoplay;
    print qq|</textarea><br>\n|;
    print qq|<input type=hidden name=mode value="iplay_after">\n|;
    &ps;

    &submit_button;
    &return_button("menu&ps=$F{'ps'}",'','button');
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub Information Play After #
sub iplay_after {
    $F{'play'} =~ s/&lt;/</g;
    $F{'play'} =~ s/&gt;/>/g;
    &write_dat($htpdat,$F{'play'});
    &iplay_before;
}

# Sub Information Character Before #
sub ichar_before {
    &error("패스워드 부정확") if $F{'ps'} ne $adps;
    &header;
    &first_box('up','170');
    &second_box('up','form');
    &title;

    &label('캐릭터 설정의 설명');
    ($character) = &open_dat($vtidat);
    $character =~ s/<br>/\n/g;
    print qq|캐릭터 설정의 설명을 편집합니다.<br>|;
    print qq|<textarea rows=15 cols=50 name=char class=text>\n|;
    print $character;
    print qq|</textarea><br>\n|;
    print qq|<input type=hidden name=mode value="ichar_after">\n|;
    &ps;

    &submit_button;
    &return_button("menu&ps=$F{'ps'}",'','button');
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub Information Character After #
sub ichar_after {
    $F{'char'} =~ s/&lt;/</g;
    $F{'char'} =~ s/&gt;/>/g;
    &write_dat($vtidat,$F{'char'});
    &ichar_before;
}

# Sub Information Virtue Before #
sub ivirt_before {
    &error("패스워드 부정확") if $F{'ps'} ne $adps;
    &header;
    &first_box('up','170');
    &second_box('up','form');
    &title;

    &label('덕목의 설명');
    ($virtue) = &open_dat($vtddat);
    $virtue =~ s/<br>/\n/g;
    print qq|덕목의 설명을 편집합니다.<br>|;
    print qq|<textarea rows=15 cols=50 name=virt class=text>\n|;
    print $virtue;
    print qq|</textarea><br>\n|;
    print qq|<input type=hidden name=mode value="ivirt_after">\n|;
    &ps;

    &submit_button;
    &return_button("menu&ps=$F{'ps'}",'','button');
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub Information Virtue After #
sub ivirt_after {
    $F{'virt'} =~ s/&lt;/</g;
    $F{'virt'} =~ s/&gt;/>/g;
    &write_dat($vtddat,$F{'virt'});
    &ivirt_before;
}

# Sub Player Data #
sub player_data {
    &error("패스워드 부정확") if $F{'ps'} ne $adps;
    &header;
    &first_box('up','420');
    &second_box('up','form');
    &title;

    &label('플레이어 데이터');
    &get_all_users;
    @alllines = map  { $_->[0] }
                sort { $a->[1] cmp $b->[1] || $a->[2] cmp $b->[2] }
                map  { [$_,(split(/<>/))[25,27]] } @alllines if $F{'sort'};
    print qq|<table align=center width=100%>\n|;
    print qq|<tr><td colspan=7>삭제하고 싶은 플레이어에 체크해 주세요.</td></tr>\n|;
    print qq|<a href=$cgiurl?mode=player_data&ps=$F{'ps'}&sort=0>[ID순으로 정렬]</a>|;
    print qq|<a href=$cgiurl?mode=player_data&ps=$F{'ps'}&sort=1>[IP순으로 정렬]</a>|;
    foreach (@alllines) {
        ($id,$nm,$ml,$ul,$ht,$bz,$os) = (split(/<>/))[0,1,4,5,25,26,27];
        if ($ml) { $ml = "<a href=mailto:$ml>$mel_img</a>" }
        if ($ul) { $ul = "<a href=$ul target=_blank>$url_img</a>" }
        $checked = $checkflag ? '' : ' checked'; $checkflag = 1;
        print qq|<tr>\n|;
        print qq|<td><input type=checkbox name="$id" value="on">$id</td>\n|;
        print qq|<td nowrap>$nm</td>|;
        print qq|<td>$ml</td>|;
        print qq|<td>$ul</td>|;
        print qq|<td>$ht</td>|;
        print qq|<td>$bz</td>|;
        print qq|<td>$os</td>|;
        print qq|</tr>\n|;
    }
    print qq|</table>\n|;
    print qq|<input type=hidden name=mode value="delete_player">\n|;
    &ps;
    &submit_button;
    &return_button("menu&ps=$F{'ps'}",'','button');
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub Delete Player #
sub delete_player {
    &error("패스워드 부정확") if $F{'ps'} ne $adps;
    &get_all_users;
    foreach (@alllines) {
        $id = (split(/<>/))[0];
        if ($F{"$id"}) { unlink("$usrdir/$id\.dat") }
    }
    $getallusersflag = 0;
    undef @alllines;
    &player_data;
}

# Sub Header #
sub header {
    print qq|Content-type: text/html\n\n|;
    print qq|<html>\n<head>\n|;
    print qq|<meta http-equiv="Content-Type" content="text/html; charset=euc_kr">\n|;
    print qq|<title>$title</title>\n|;
    &style;
    print qq|</head>\n$body\n|;
    $headflag = 1;
}

# Sub Footer #
sub footer {
    if ($_[0]) {
        print qq|<br>\n</body>\n</html>\n|;
    }
    else {
        # 저작권표시. 절대 삭제하지 말아주세요!
        # 여기에 링크를 넣는 경우, Missing Link와 같은행에 하지말고,
        # 반드시 줄을 바꿔서 별개의 행으로 넣어주세요.
        # 개조자의 링크를 붙이는 경우, 개조자의 앞에 반드시「Edit:」를 붙여주세요.
        print qq|<br><center><font color=$tbl_lnc>PeoPle For Administer Ver $ver<br>\n|;
        print qq|■ <a href="http://www.area-s.com/" target="_blank" title="PeoPle의 본가 배포원">MISSING LINK</a> ■<br>|;
        print qq|■ 한글화 = <a href="http://www.adonas.com/" target="_blank">adonas의 작업실</a> ■<br>|;
        print qq|■ 1.6 한글화 = <a href="http://side1.uu.st" target="_blank">쥬도네 고물상</a> ■|;
        print qq|</font></center>\n</body>\n</html>\n|;
    }
}

# Sub Style #
sub style {
    print qq|<STYLE TYPE="text/css">\n|;
    print qq|<!--\n|;
    print qq|A:link    {text-decoration:none;color:$nlc_clr;font-weight:bold }\n|;
    print qq|A:hover   {text-decoration:none;color:$vlc_clr;font-weight:bold }\n|;
    print qq|A:visited {text-decoration:none;color:$alc_clr;font-weight:bold }\n|;
    print qq|body,tr,td,th { font-size:$fnt_sze }\n|;
    print qq|.button { font-size:$but_sze;border:solid;border-width:3pt 1pt;border-color:$tbl_lnc;background-color:#FFCCFF }\n|;
    print qq|.text   { font-size:$txb_sze;border:solid;border-width:1pt;border-color:$tbl_lnc;background-color:$txb_clr }\n|;
    print qq|-->\n|;
    print qq|</STYLE>\n|;
}

# Sub First Box #
sub first_box {
    if ($_[0] eq 'up') {
        print qq|<div align=center>\n|;
        print qq|<table border=0 cellspacing=0 cellpadding=0 bgcolor=$tbl_bgc width=$_[1]>\n|;
        print qq|<tr>\n|;
        print qq|<td><img src=$img/lt.gif width=8 height=8></td>\n|;
        print qq|<td><img src=$img/1p.gif></td>\n|;
        print qq|<td align=right><img src=$img/rt.gif width=8 height=8></td>\n|;
        print qq|</tr>\n|;
        print qq|<tr>\n|;
        print qq|<td><img src=$img/1p.gif></td>\n|;
        print qq|<td>\n|;
    }
    if ($_[0] eq 'down') {
        print qq|</td>\n|;
        print qq|<td><img src=$img/1p.gif></td>\n|;
        print qq|</tr>\n|;
        print qq|<tr>\n|;
        print qq|<td><img src=$img/lb.gif width=8 height=8></td>\n|;
        print qq|<td><img src=$img/1p.gif></td>\n|;
        print qq|<td align=right><img src=$img/rb.gif width=8 height=8></td>\n|;
        print qq|</tr>\n|;
        print qq|</table>\n|;
        print qq|</div>\n|;
    }
}

# Sub Second Box #
sub second_box {
    if ($_[0] eq 'up') {
        print qq|<table border=1 cellspacing=0 cellpadding=5 width=100% bordercolorlight=$tbl_lnc bordercolordark=$tbl_lnc bordercolor=$tbl_lnc>\n|;
        print qq|<tr>\n|;
        print qq|<form method=$method action=$cgiurl>\n| if $_[1];
        print qq|<td>\n|;
    }
    if ($_[0] eq 'middle') {
        print qq|</td>\n|;
        print qq|</tr>\n|;
        print qq|<form method=$method action=$cgiurl>\n|;
        print qq|<tr>\n|;
        print qq|<td>\n|;
    }
    if ($_[0] eq 'down') {
        print qq|</td>\n|;
        print qq|</tr>\n|;
        print qq|</form>\n|;
        print qq|</table>\n|;
    }
}

# Sub Title #
sub title {
    return if !$def_ti;
    print qq|<p align=center><img src=$img/$ttl_img width=$ttl_wth height=$ttl_hgt></p>|;
}

# Sub Label #
sub label {
    print qq|<div align=center>\n|;
    print qq|$hrt_img\n|;
    print qq|$_[0]\n|;
    print qq|$hrt_img\n|;
    print qq|</div>\n|;
    print qq|<br>\n|;
}

# Sub Password #
sub ps {
    print qq|<input type=hidden name=ps value="$F{'ps'}">\n|;
}

# Sub Submit Button #
sub submit_button {
    print qq|<br>\n|;
    print qq|<div align=right>\n|;
    print qq|<input type=submit value="$sub_lbl" class=button>\n|;
    print qq|</div>\n|;
}

# Sub Return Button #
sub return_button {
    $type = $_[2];
    $type = 'link' if $def_rb;
    print qq|<a href=$cgiurl?mode=$_[0]>$bak_lbl</a><br>\n| if $type eq 'link';
    print qq|<div align=center><input type=button value="$bak_lbl" onClick="history.back()" class=button></div>| if $type eq 'button';
    print qq|<br>\n| if $_[1] eq 'br';
}

# Sub Home Button #
sub home_button {
    if (!$def_ho) { return }
    print qq|<br><center>|;
    print qq|<a href=$hom_url target=$hom_tgt>$hom_lbl</a><br>\n|;
    print qq|</center>\n|;
}

# Sub Open Dat #
sub open_dat {
    open(IN,"$_[0]") || &error("$_[0]읽기 에러:$_[0]가 존재하지 않거나 퍼미션이 틀립니다.");
    local(@lines) = <IN>;
    close(IN);
    return @lines;
}

# Sub Write Dat #
sub write_dat {
    open(OUT,">$_[0]") || &error("$_[0]쓰기 에러:$_[0]가 존재하지 않거나 퍼미션이 틀립니다.");
    shift(@_);
    print OUT @_;
    close(OUT);
}

# Sub Get All Users #
sub get_all_users {
    return if $getallusersflag;
    opendir(DIR,"$usrdir") || &error("유저 데이터 읽기 에러:$usrdir라는 이름의 유저 데이터용 디렉토리가 없거나 퍼미션이 틀립니다.");
    @userfiles = sort grep /.+\.dat/,readdir(DIR);
    closedir(DIR);
    foreach (@userfiles) {
        open(IN,"$usrdir\/$_") || &error("$usrdir\/$_을 열 수 없습니다.");
        ($line) = <IN>;
        push(@alllines,$line);
        close(IN);
    }
    $getallusersflag = 1;
}

# Sub Set Cookie #
sub set_cookie {
    # 쿠키는 90일간 존재　
    ($secg,$ming,$hourg,$mdayg,$mong,$yearg,$wdayg,$ydayg,$isdstg) = gmtime(time + 90*24*60*60);
    $yearg += 1900;
    if ($secg  < 10) { $secg  = "0$secg";  }
    if ($ming  < 10) { $ming  = "0$ming";  }
    if ($hourg < 10) { $hourg = "0$hourg"; }
    if ($mdayg < 10) { $mdayg = "0$mdayg"; }
    $month = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')[$mong];
    $youbi = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')[$wdayg];
    $date_gmt = "$youbi, $mdayg\-$month\-$yearg $hourg:$ming:$secg GMT";
    $cook = "ps\:$F{'ps'}";
    print "Set-Cookie: $cookname=$cook; expires=$date_gmt\n";
}

# Sub Get Cookie #
sub get_cookie { 
    @pairs = split(/\;/,$ENV{'HTTP_COOKIE'});
    foreach $pair (@pairs) {
        local($name, $value) = split(/\=/, $pair);
        $name =~ s/ //g;
        $DUMMY{$name} = $value;
    }
    @pairs = split(/\,/,$DUMMY{$cookname});
    foreach $pair (@pairs) {
        local($name, $value) = split(/\:/, $pair);
        $COOKIE{$name} = $value;
    }
    $c_ps = $COOKIE{'ps'};
}

# Sub Error #
sub error {
    $_[1] || &unlock;
    if (!$headflag) { &header }
    print qq|<center>\n|;
    print qq|<hr width=80%>\n|;
    print qq|<B><font color=#FF0000>$_[0]</font></B>\n|;
    print qq|<hr width=80%>\n|;
    print qq|</center>\n|;
    &footer;
    exit;
}

# Sub Lock #
sub lock {
    return if !$lockkey;
    local($flag) = 10;
    if    ($lockkey == 1) {
        rmdir($lockfile) if (time - (stat($lockfile))[9] > 60);
        while (!mkdir($lockfile,0755)) {
            --$flag or &error('현제, 서버가 붐비고 있습니다',1);
            sleep(1);
        }
    }
    elsif ($lockkey == 2) {
        unlink($lockfile) if (time - (stat($lockfile))[9] > 60);
        while (!symlink(".",$lockfile)) {
            --$flag or &error('현제, 서버가 붐비고 있습니다',1);
            sleep(1);
        }
    }
}

# Sub Unlock #
sub unlock {
    if    ($lockkey == 1) { rmdir($lockfile)  }
    elsif ($lockkey == 2) { unlink($lockfile) }
}

# Sub Decode #
sub decode {
    if ($ENV{'REQUEST_METHOD'} eq "POST") {
        read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
        @pairs = split(/&/, $buffer);
    } else { @pairs = split(/&/, $ENV{'QUERY_STRING'}) }

    foreach $pair (@pairs) {
        ($name, $value) = split(/=/, $pair);
        $name =~ tr/+/ /;
        $name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        # &jcode::convert(*name,'sjis');
        # &jcode::convert(*value,'sjis');

        $value =~ s/</&lt;/g;
        $value =~ s/>/&gt;/g;
        $value =~ s/△/▲/g;
        $value =~ s/\,/,/g;
        $value =~ s/\r\n/<br>/g;
        $value =~ s/\r/<br>/g;
        $value =~ s/\n/<br>/g;

        $F{$name} = $value;
    }
}
# ######################### 서브 루틴 종료 #########################
