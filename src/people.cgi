#!/usr/bin/perl

use utf8;  # Perl 내부에서 UTF-8 지원
binmode(STDOUT, ":encoding(EUC-KR)");  # 출력 인코딩을 EUC-KR로 설정


# ↑서버에 맞게 변경해 주세요.
# 보통 (#!/usr/local/bin/perl) 또는 (#!/usr/bin/perl)

# ##################################################################
# PeoPle
    $ver = '1.6';
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

# ############################ 설정개시 ############################

# ↓유저 데이터를 보관할 디렉토리명(보안을 위해 반드시 변경해주세요)
# 변경한 이름과 같은 이름의 디렉토리를 people.cgi와 같은 장소에 작성
# 퍼미션은 777 또는 707로 합니다. (주 : 디렉토리=폴더)

$usrdir  = '/var/www/html/user';    # 주의：주소는 아니고 디렉토리명만

# ↓PeoPle에서 사용하는 모든 그림을 보관하는 디렉토리 입니다.
# 절대주소(http://로 시작되는 주소)도 상대주소도 상관없습니다.
# 초기값은 people.cgi와 같은 장소에 배치 하도록 되있습니다.
# 프로바이더(서버)에 따라서는 cgi-bin아래에 그림 디렉토리를
# 두는 것을 금지하고 있는 경우가 있습니다. 그런 경우에는 cgi-bin보다
# 위쪽에 그림 디렉토리를 배치하고 주소를 변경해 주세요.

$img     = '/img';       # 주의：마지막에 슬레쉬(/)를 붙이지 말아주세요.

$hom_url = 'http://';     # 돌아올 홈의URL
$hom_tgt = '_self';       # 돌아올 홈의 타겟(톱='_top',자신='_self',신규='_blank')
$hom_lbl = '홈';          # 돌아올 홈의 라벨
$def_ho  = 1;             # 돌아올 홈의 버튼을 표시한다(yes = 1,no = 0)

$lockkey = 1;             # 파일의 락(rmdir = 1,symlink = 2,no = 0)
                          # symlink가 잘되지 않는 경우엔 rmdir을 사용해 주세요.

$adps     = '1234';       # 관리자 패스워드(변경필수)

$title    = 'PeoPle';     # 타이틀명(브라우저 위쪽에 표시)
$body     = '<body bgcolor=#FFFFFF text=#000000>';    # 보디 태그

$fnt_sze  = '8pt';        # 폰트 사이즈

$mtb_wth  = 220;          # 메인테이블의 폭
$stb_wth  = 340;          # 작은(팝업) 창의 테이블의 폭
$tbl_bgc  = '#FFDFFF';    # 테이블의 배경색
$tbl_lnc  = '#FF66FF';    # 태이블의 라인의 색

$nlc_clr  = '#CC00CC';    # 링크색(방문전)
$vlc_clr  = '#990099';    # 링크색(방문후)
$alc_clr  = '#FF0000';    # 링크색(방문중)

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

$def_cp   = 1;            # 패스워드를 암호화한다(yes=1,no=0)
                          # 설정을 변경하면 이전의 패스워드는 무효가 됩니다.
                          # 서버를 이전하는 경우, 이전의 암호화된 패스워드는 무효가 되는 경우가 있습니다.
                          # 암호화 하면 패스워드를 잊는경우 알아내기는 불가능합니다. 
                          # 서버에 따라서 암호화 할 수 없는 경우도 있습니다.

$def_ip   = 0;            # IP제한을 건다(yes=1,no=0)
$def_ei   = 'key';        # IP제한을 걸었을 때의, (관리자용)취소 키.
                          # IP제한을 하는경우 이설정을 반드시 변경.
                          # 반각 소문자 알파벳, 숫자만 사용가능
                          # PASSWORD의 앞에 이 키를 붙이면 IP제한을
                          # 취소하고 신규등록을 할 수 있습니다.
                          # 등록후, 키는 패스워드에서 빠집니다.
                          # 예：key0000→IP제한 취소→등록→PASS=0000
                          # IP제한으로 신규등록 할 수 없는 사람이 있는 경우,
                          # 관리자가 이 방법으로 대신하여 신규등록을 해주세요.

$def_mp   = 100;          # 등록자 제한을 하는경우(yes=사람수,no=0)(100명 까지를 추천)

$def_nb   = 12;           # 등록 할 수 있는 이름의 최대 바이트 수        (전각 1문자 = 2바이트)
$def_ib   = 200;          # 등록 할 수 있는 자기소개의 최대 바이트 수    (전각 1문자 = 2바이트)
$def_pn   = 10;           # 등록 할 수 있는 애완동물의 이름의 최대 바이트 수 (전각 1문자 = 2바이트)

$def_ml   = 1;            # 휴대전화 메일 기능을 사용한다(yes=1,no=0)
                          # 이 기능을 사용하는 것에 따라 플레이어 끼리의
                          # 커뮤니케이션이 가능하게 합니다.
                          # 하지만 커뮤니 케이션은(특히 남녀사이의)
                          # 트러블이 일어날 가능성이 있기 때문에,
                          # 관리자의 책임하에 사용하도록 해주세요.

$def_eb   = 1;            # 메일을 보낼 수 있는 대상범위(전항에 따릅니다)
                          # 0 = 연인 만
                          # 1 = 연인과 전의 연인(추천)
                          # 2 = 접속상대전원(한쪽에서만 보낼 수 있는 경우가 있습니다)

$def_st   = 0;            # 독자적인 CSS파일을 읽습니다(yes=1,no=0)
$def_su   = 'xxx.css';    # CSS파일의 주소(절대주소or상대주소)
                          # PeoPle로 사용하고 있는 프로파티명
                          # text   (사용방법:textbox,select,textarea)
                          # button (사용방법:button)

$def_rb   = 0;            # 뒤로 버튼을 모두 링크 버튼으로 한다(yes=1,no=0)
                          # 서버에 따라서는 뒤로 버튼이 재대로 기동하지 않는 경우도 있습니다.
                          # 그런 경우에는 버튼을 링크 버튼으로 변경하여 주세요.

$def_pc   = 0;            # 처음 화면에 거주자의 수를 표시한다.(yes=1,no=0)
                          # 서버가 무거운 경우에는 이용을 중지하여 주세요.

$def_ic   = 0;            # 아이콘을 사용한다(yes=1,no=0)
$def_is   = 70;           # 아이콘을 표시할 공간의 폭
$def_lt   = 0;            # 아이콘 일람을 사용한다(yes=1,no=0)
$icn_lt   = 'http://';    # 아이콘 일람의URL(자신이 작성한 HTML에 링크)
@icn_mn   = ('××','●●');   # 아이콘의 이름(남)
@icn_mf   = ('1.gif','2.gif'); # 아이콘의 파일(파일명만)(남)
@icn_wn   = ('○○','△△');   # 아이콘의 이름(여)
@icn_wf   = ('3.gif','4.gif'); # 아이콘의 파일(파일명만)(여)
                          # 아이콘 파일은 화상 디렉토리에 넣어주세요.

$def_pj   = 50;           # 거주자 일람 1페이지에 표시할 사람수
$def_fm   = 5;            # 초기소지금
$def_yr   = 24;           # 몇시간 단위로 급여하는가
$def_ag   = 1;            # 연령이 1오르는데 걸리는 일 수
$def_oa   = 125;          # 연령의 상한(높을수록 수명이 늘어난다)
$def_ya   = 70;           # 최저사망연령(높을수록 수명이 늘어난다)
$def_lc   = 1;            # 전회부터 몇시간 경과하면 다시 러브체크 하는가?(0이상)
$def_ch   = 2;            # 전회부터 몇시간 경과하면 다시 격려할 수 있는가?(0이상)
$def_il   = 5;            # 몇일간 격려하지 않으면 병에 걸리는가?(1이상)
$def_dd   = 7;            # 몇일간 격려하지 않으면 죽는가?(1이상)
$def_om   = 30;           # 이력의 최대 보존수(1이상)
$def_nx   = 50;           # 거주자뉴스 최대 보존수(1이상)
$def_pr   = 3;            # 선물의 소지 상한(1이상)
$def_gp   = 3;            # 선물을 주는 확률(1/x)
$def_bb   = 1;            # 임신해서 몇일이 지나면 아기를 낳는가?
$def_pf   = 3;            # 애완동물 먹이의 소지 상한(1이상)
$def_pe   = 2;            # 애완동물은 몇일에 한개의 먹이를 먹는가?(1이상)
$def_pl   = 3;            # 애완동물은 먹이 없이 얼마나 살아갈 수 있는가?(1이상)
$def_jb   = '무직';       # 시작시의 직업
$def_nw   = '이제 막 태어났습니다'; # 시작시의 상태

# ############################ 설정종료 ############################

# ############################ 응용설정 ############################
# 이하의 항목은 보통 변경 불필요

# ---------- FILE PASS
$cgiurl  = './people.cgi'; # people.cgi의 주소(보통 변경 불필요) 755(705)
$newcgi  = './new.cgi';    # new.cgi의 주소   (보통 변경 불필요) 644
$luvcgi  = './lovers.cgi'; # lovers.cgi의 주소(보통 변경 불필요) 644

$jobdat  = '/var/www/html/dat/job.dat';
$itmdat  = '/var/www/html/dat/itm.dat';
$chddat  = '/var/www/html/dat/chd.dat';
$elsdat  = '/var/www/html/dat/els.dat';
$dtedat  = '/var/www/html/dat/dte.dat';
$pztdat  = '/var/www/html/dat/pzt.dat';
$petdat  = '/var/www/html/dat/pet.dat';
$htpdat  = '/var/www/html/dat/htp.dat';
$vtidat  = '/var/www/html/dat/vti.dat';
$vtddat  = '/var/www/html/dat/vtd.dat';
$nwsdat  = '/var/www/html/dat/nws.dat';

$lockfile= './ppllock';    # 락파일명

$method  = 'POST';         # POST or GET *POST추천

$cookname= 'PPL';          # 쿠키명

$def_dh  = 5;              # 사망 체크 시간(1-24)
$def_lj  = 5;              # 일을 농땡이칠 확률(%)(성실함이 낮은 사람은 추가)
$def_pb  = 10;             # 선물에 의해 오르는 러브 보너스
$def_lm  = 50;             # 호감도 몇%로 연애대상이 되는가?(1이상)
$def_bs  = 10;             # 동성애도(높을수록 동성애가 낮아진다(1이상))
$def_ac  = 2;              # 몇회에 1번 자신이 자신이 직접 상대를 찾아가는가(가장 소극적인 사람이)
$def_lo  = 3;              # 몇번 고백하고 실패하면 단념하는가(가장 소극적인 사람이)
$def_af  = 7;              # 전체적인 바람도(낮을수록 바람도가 높다(4이상))
$def_dv  = 5;              # 싸움 보너스(높을 수록 싸움이 많아진다(0-10))
$def_ld  = 6;              # 서로의 러브 포인트가 몇점 이하면 해어지는가
$def_mr  = 7;              # 서로의 러브 포인트가 몇점 이상이면 결혼하는가
$def_pg  = 9;              # 서로의 러브 포인트가 몇점 이상이면 임신하는가
$def_ab  = 4;              # 출산 후 두명의 러브 포인트(높을수록 재임신하기 쉽다)
$def_pm  = 12;             # 러브 포인트 상한
$def_ht  = -3;             # 러브 포인트가 몇점 이하면 차이는가
$def_gj  = 10;             # 급료로 임시 보너스가 나오는 확률(%)
$def_bp  = 3;              # 임시 보너스는 급료의 x배

$smw_wth = 380;            # 작은(팝업)창의 가로폭
$smw_hgt = 420;            # 작은(팝업)창의 세로폭

$fce_wth = 12;             # 얼굴 그림의 가로폭
$fce_hgt = 12;             # 얼굴 그림의 세로폭
$sex_wth = 10;             # 성별 그림의 가로폭
$sex_hgt = 10;             # 성별 그림의 세로폭
$pet_wth = 10;             # 애완동물 그림의 가로폭
$pet_hgt = 10;             # 애완동물 그림의 세로폭

# 하트의 화상
$hrt_img = qq|<img src="$img/heart.gif" width=12 height=12>|;
# 돈의 화상
$mny_img = qq|<img src="$img/money.gif" width=10 height=10>|;
# 선물의 화상
$prz_img = qq|<img src="$img/present.gif" width=14 height=12>|;
# 남자의 화상
$man_img = qq|<img src="$img/man.gif" width="$sex_wth" height="$sex_hgt">|;
# 여자의 화상
$wmn_img = qq|<img src="$img/woman.gif" width="$sex_wth" height="$sex_hgt">|;
# 애완동물 먹이의 화상
$pfd_img = qq|<img src="$img/petfood.gif" width=10 height=10>|;
# 메일의 화상
$mel_img = qq|<img src="$img/mail.gif" border=0 width=10 height=10>|;
# 홈페이지 주소의 화상
$url_img = qq|<img src="$img/url.gif" border=0 width=10 height=10>|;

# 초기이력의 설명(마지막의 HTP는 삭제하지 말아주세요)
$hismsg= <<"HTP";

<br>당신의 주인에게 일어난 사건등을 이력에 보존합니다.<br>
최대 보존수는 $def_om건 입니다.<br>

HTP
# ↑삭제금지

# ############################ 설정종료 ############################

# ########################### 데이터개시 ###########################
# 이하의 항목은 보통 변경 불필요

$def_tv = 8;               # 매력의 수
# 매력 리스트
@VT = ('상냥함','용기','용모','지성','재력','건강','정력','성실');
# 행동지수치(수치분만 가산된다(1개의 항목의 합계는 4이하로 설정해주세요))
# 동성애
@BS = (     1,     0,     1,     1,     0,     0,     0,     1);
# 적극성
@AC = (     0,     1,     0,     0,     1,     1,     1,     0);
# 바람도
@AF = (     0,     1,     1,     0,     0,     0,     1,     0);
# 얼굴그림
@BF = ('b_sick.gif','b_blue.gif','b_normal.gif','b_good.gif','b_fun.gif','b_love.gif');
@GF = ('g_sick.gif','g_blue.gif','g_normal.gif','g_good.gif','g_fun.gif','g_love.gif');
# 얼굴설명
@FL = ('아픕니다','우울합니다','보통입니다','기분이 좋습니다','행복합니다','사랑을 하고 있습니다');
# 직업레벨
@JL = ('신입','말단','중견','유명','거물','카리스마');
# 상품의 설명
%SL = ('C' => '메일용','S' => '데이트용(2)','T' => '데이트용(1)','W' => '결혼용','Y' => '출산용','Z' => '기타');

$def_cb   = 2;            # 격려하면 올라가는 보너스의 최대치
# 격려 메세지($def_cb에 대응 보너스 점수는 왼쪽부터 0,1,2‥)
@CL = ('그다지 격려를 하지 못한 것 같습니다','조금 기운이 난 것 같습니다','기운을 많이 차린 것 같습니다');
@MP = ('부인','남편');        # 결혼상대의 호칭

# ########################### 데이터종료 ###########################

# ####################### 메인 프로그램 개시 #######################
&error("유저 디렉토리명을 변경해 주세요. [$cgiurl의 29행]") if $usrdir eq 'userdata';
&error("관리 패스워드를 변경해 주세요. [$cgiurl의 50행]") if $adps eq '0000';
&decode;
if ($F{'id'} =~ /\W/) { &error('부정확한 입력입니다') }
if ($F{'mode'} eq 'new_regist'   ||
    $F{'mode'} eq 'set_regist'   ||
    $F{'mode'} eq 'new_job'      ||
    $F{'mode'} eq 'set_new_job'  ||
    $F{'mode'} eq 'pet_name'     ||
    $F{'mode'} eq 'set_pet_name' ||
    $F{'mode'} eq 'info_virtue'  ||
    $F{'mode'} eq 'select_icon'  ||
    $F{'mode'} eq 'set_icon'     ||
    $F{'mode'} eq 'set_virtue') {

    open(my $fh, "<:encoding(EUC-KR)", $newcgi) or die "Cannot open $newcgi: $!";
    my $code = do { local $/; <$fh> };
    close($fh);
    
    eval $code;
    die "Error loading $newcgi: $@" if $@;
}

if (!$F{'mode'})                { &start_view     }
else                            { &{$F{'mode'}}   }
&unlock;
exit;
# ####################### 메인 프로그램 종료 #######################

# ######################### 서브루틴 개시 ##########################

# Sub Start View #
sub start_view {
    &header('java');
    &first_box('up');
    &second_box('up','form');
    &title;
    &info_button;
    &new_regist_button;

    &get_cookie;
    $on_click = qq|onClick="return opWin('$cgiurl?mode=id_list','win4')"|;
    print qq|ID 【<a href=$cgiurl?mode=id_list $on_click target=_blank>ID LIST</a>】<br>\n|;
    print qq|<input type=text name=id class=text size=$stx_wth value="$c_id">\n|;
    print qq|<br>\n|;
    print qq|패스워드<br>\n|;
    print qq|<input type=password name=ps class=text size=$stx_wth value="$c_ps">\n|;
    print qq|<input type=hidden name=mode value="play_view">\n|;

    &submit_button;
    &news_button;
    &count_players if $def_pc;
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub Count Players #
sub count_players {
    &get_all_users;
    $ttl_count = @alllines;
    $wmn_count = grep { $_ } map { (split(/<>/))[3] } @alllines;
    $man_count = $ttl_count - $wmn_count;
    print qq|<br>\n|;
    print qq|전 거주자：$ttl_count명 ($man_img：$man_count명 $wmn_img：$wmn_count명)<br>\n|;
}

# Sub Play View #
sub play_view {
    &set_cookie if $F{'mode'} eq 'play_view';
    &get_iuser($F{'id'});
    &regist_virtue,return if !$iv || !$uv;
    &header('java');
    &first_box('up');
    &second_box('up','form');
    &title;
    if ($nw) { &msg("$nw"); $nw = '' }
    &people_action if $F{'mode'} eq 'play_view';
    &iprofile;
    &second_box('middle');
    &action_select;
    &submit_button;
    &player_list_button;
    &history_button;
    &news_button;
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
    &set_iuser;
}

# Sub Regist Virtue #
sub regist_virtue {
    $count = 1;
    &header('java');
    &first_box('up');
    &second_box('up','form');
    &title;
    &info_button;
    &virtue_button;
    &label('캐릭터 설정');
    print &open_dat($vtidat);
    print qq|<br><br>\n|;
    foreach $who ('i','u') {
        &label('자신의 매력의 순위')   if $who eq 'i';
        &label('상대에게 바라는 우선순위') if $who eq 'u';
        print qq|<table align=center border=0 cellspacing=5 cellpadding=0>\n|;
        foreach (0 .. $def_tv - 1) {
            print qq|<tr>\n| if $count == 1;
            print qq|<td>$VT[$_]</td>\n|;
            print qq|<td><input type=textbox class=text size=1 name=$who$_>위</td>\n|;
            print qq|</tr>\n| if $count >= 2 || $count >= $def_tv - 1;
            if ($count >= 2) { $count = 1 } else { $count++ }
        }
        print qq|</table>\n|;
        print qq|<br>\n| if $who eq 'i';
    }
    print qq|<input type=hidden name=mode value="set_virtue">\n|;
    &id_ps;

    &submit_button;
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub How To Play #
sub how_to_play {
    &header;
    &first_box('up','smallwindow');
    &second_box('up','form');
    &title;
    &label('설명서');
    print &open_dat($htpdat);
    &second_box('down');
    &first_box('down');
    &footer('nocopyright');
}

# Sub Cheer #
sub cheer {
    &get_iuser($F{'id'});
    local($age) = int((time - $t1) / (60 * 60));
    if ($age < $def_ch) {
        &msg("격려한지 얼마되지 않았습니다");
    }
    elsif ($age >= $def_il * 24) {
        $fc   = 2;
        $t1   = time;
        &msg("병이 나았습니다");
    }
    else {
        srand($$ | time);
        $dice = int(rand($def_cb + 1));
        $fc  += $dice;
        &msg("$CL[$dice]");
        $fc   = $#FL - 1 if $fc >= $#FL;
        $t1   = time;
    }
    $fl = '';
    &play_view;
}

# Sub Shopping #
sub shopping {
    &get_iuser($F{'id'});
    @itmlines = &open_dat($itmdat);
    $fl='SHP'; &set_iuser;
    &header;
    &first_box('up');
    &second_box('up','form');
    &title;
    &label('쇼핑');

    print qq|소지금 $mny_img：$mn G\n|;

    foreach (0 .. $#itmlines) {
        $ini = $iin;
        ($inm,$ipc,$iim,$iin) = split(/<>/,$itmlines[$_]);
        $checked = $_ == 0 ? ' checked' : '';
        print qq|<hr class=text>\n| if $ini ne $iin;
        print qq|$SL{"$iin"}<br>\n| if $ini ne $iin && $SL{"$iin"};
        print qq|<input type=radio name=item value="$_"$checked>|;
        print qq|<img src="$img/$iim"> |;
        print qq|$inm $mny_img：$ipc G<br>\n|;
    }
    undef @itmlines;

    print qq|<input type=hidden name=mode value="buy">\n|;
    &id_ps;
    &submit_button;
    &return_button("play_view&id=$F{'id'}&ps=$F{'ps'}",'','button');
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub Buy #
sub buy {
    &get_iuser($F{'id'});
    if ($fl ne 'SHP') { &play_view; return }
    $fl = '';
    @itmlines = &open_dat($itmdat);
    ($inm,$ipc,$iim,$iin,$ipt,$isx) = split(/<>/,$itmlines[$F{'item'}]);
    undef @itmlines;
    &error("소지금이 부족합니다") if $mn < $ipc;
    @ft = split(/,/,$ft);
    $sex = $sx ? '남성' : '여성';
    if ($isx ne '' && $isx ne $sx) { &error("그 아이템은 $sex용 입니다") }
    elsif ($iin eq 'A') {
        if ($pr < $def_pr) { $pr++ }
        else { &error("더 이상 선물을 보관할 수 없습니다") }
    }
    elsif ($iin eq 'F') {
        if ($pfd + $ipt <= $def_pf) { $pfd += $ipt }
        else { &error("더 이상 애완동물의 먹이를 보관할 수 없습니다") }
    }
    elsif ($iin eq 'E') {
        if (!$pim) {
            $pim = $iim; $pdt = $ipt; $ptm = time;
            &add_record("애완동물을 기릅니다");
            $fb .= $iin if $fb !~ /$iin/;
        }
        else { &error("이미 애완동물을 기르고 있습니다") }
    }
    elsif ($iin eq 'L') {
        require $luvcgi;
        &love_potion;
    }
    else {
        foreach (@ft) {
            ($ftn) = split(/△/);
            &error("$inm(은/는) 이미 소유하고 있습니다") if $ftn eq $inm;
        }
        $ft = join(',',@ft,"$inm△$iim");
        if ($iin =~ /(C|S|T|W|Y)/) {
            $ini = $iin . $ipt;
            $fb .= $ini if $fb !~ /$ini/;
        }
        $fp += $ipc;
    }
    &msg("$inm(을/를) 사줬습니다") if $iin ne 'L';
    $mn -= $ipc;
    &play_view;
}

# Sub Introduce #
sub introduce {
    &get_iuser($F{'id'});
    $fl='IDC'; &set_iuser;
    &header;
    &first_box('up');
    &second_box('up','form');
    &title;
    &label('자기소개');
    print qq|다른 주인에게 자기소개를 하는 것이 가능합니다.<br>\n|;
    print qq|엔터, 태그는 무효입니다.<br>\n|;
    print qq|<textarea name=in cols=30 rows=5 class=text>\n|;
    print qq|$in|;
    print qq|</textarea><br>\n|;
    print qq|메일 (임의)<br>|;
    print qq|<input type=text name=ml value="$ml" size=$ltx_wth class=text><br>\n|;
    print qq|홈페이지 주소 (임의)<br>|;
    print qq|<input type=text name=ul value="$ul" size=$ltx_wth class=text>\n|;
    print qq|<input type=hidden name=mode value="set_introduce">\n|;
    &id_ps;
    &submit_button;
    &return_button("play_view&id=$F{'id'}&ps=$F{'ps'}",'','button');
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub Set Introduce #
sub set_introduce {
    &get_iuser($F{'id'});
    if ($fl ne 'IDC') { &play_view; return }
    &error("자기소개의 길이는 반각 $def_ib글자 까지") if length $F{'in'} > $def_ib;
    &error("메일의 입력이 부정확 합니다") if  $F{'ml'} && $F{'ml'} !~ /(.*)\@(.*)\.(.*)/;

    &get_all_users;

    ($mailcheck) = grep { $_->[0] ne $F{'id'} }
                   grep { $_->[1] && $_->[1] eq $F{'ml'} }
                   map  { [(split(/<>/))[0,4]] } @alllines if $F{'ml'};
    ($urlcheck)  = grep { $_->[0] ne $F{'id'} }
                   grep { $_->[1] && $_->[1] eq $F{'ul'} }
                   map  { [(split(/<>/))[0,5]] } @alllines if $F{'ul'};

    if ($mailcheck) { &error("그 메일은 이미 사용중 입니다") }
    if ($urlcheck)  { &error("그 홈페이지 주소는 이미 사용중 입니다") }

    $fl =  '';
    $in =  $F{'in'};
    $ml =  $F{'ml'};
    $ul =  $F{'ul'};
    $in =~ s/<br>//g;
    &play_view;
}

# Sub Mail Form #
sub mail_form {
    &get_iuser($F{'id'});
    $fl='MFM'; &set_iuser;
    &header('java');
    &first_box('up');
    &second_box('up','form');
    &title;
    &label('메일을 보낸다');
    print qq|누구에게 메일을 보낼까요?<hr class=text>\n|;
    # 자신의 연인 리스트
    if ($def_eb) { $lv = $bl }
    @ilv = split(/△/,$lv);
    print qq|<input type=radio name=uid checked value=''>아무에게도 보내지 않는다<br>\n|;
    foreach (@ilv) {
        if ($def_eb) { ($uid,$unm,$ulp) = split(/,/) }
        else {
            ($uid,$usx,$unm,$ulp) = split(/,/);
            $mp = $uid eq $hw ? " [$MP[$sx]]" : '';
            &name_title($usx);
        }
        if ($def_eb == 1 && $ulp ne 'luv') { next }
        print qq|<input type=radio name=uid value="$uid">|;
        $on_click = qq|onClick="return opWin('$cgiurl?mode=uprofile&id=$uid','win6')"|;
        print qq|　 <a href="$cgiurl?mode=uprofile&id=$uid" $on_click target=_blank>$unm$unt$mp</a><br>\n|;
        print qq|\n|;
    }
    print qq|<hr class=text>\n|;
    print qq|<textarea name=lt cols=30 rows=5 class=text></textarea><br>\n|;
    $checked = $rr ? ' checked' : '';
    print qq|<input type=checkbox name=x$checked>메일 수신거부\n|;
    print qq|<input type=hidden name=mode value="send_mail">\n|;
    &id_ps;
    &submit_button;
    &return_button("play_view&id=$F{'id'}&ps=$F{'ps'}",'','button');
    &second_box('down');
    &first_box('down');
    &home_button;
    &footer;
}

# Sub Send Mail #
sub send_mail {
    &get_iuser($F{'id'});
    if ($fl ne 'MFM') { &play_view; return }
    &error("메일의 길이는 반각 $def_ib글자 까지") if length $F{'lt'} > $def_ib;
    &error("메일의 내용을 입력하지 않았습니다") if !$F{'lt'} && $F{'uid'} ne '';
    $F{'lt'} =~ s/<br>//g;
    $fl =  '';
    $rr = $F{'x'} ? 1 : 0;
    if ($F{'uid'} ne '') {
        &get_uuser($F{'uid'});
        if ($dead) { &play_view; return }
        if ($urr)  { &error('상대의 메일은 수신거부가 되어있습니다') }
        elsif ($ufb =~ /Ca/ && $ufb =~ /Cb/) {
            &add_record("$nm：「$F{'lt'}」",'other');
            &add_record("송신：「$F{'lt'}」");
            &msg("메일을 보냈습니다");
            $unw  .= "메일을 받았습니다<br>";
        }
        else { &error('상대는 메일을 볼수 없습니다') }
        &set_uuser;
    }
    &play_view;
}

# Sub PeoPle Action #
sub people_action {
    # 날자 체크
    &date_check;
    srand($sec);
    if (!$pg) { $lp-- if !$lv && $lp > 1 } # 연인이 없는 사람은「상대를 찾는다」로

#    if (!$pg && !$sic) {
    if (time - $t2 >= $def_lc * 60 * 60 && !$pg && !$sic) {
        require $luvcgi;
        $t2  = time;
        if ($lp > 1) { &lovers     } # 연인
        else         { &find_lover } # 상대를 찾는다
        if (!$msg)   { &special_action }
        &pet_action;
    }
    # 임신중
    &birth;
    # 일
    &working;
    &write_news if @newslines;
}

# Sub Birth #
sub birth {
    return if !$pg;
    local($age) = &get_age($t2);
    return if $def_bb > $age;

    $child = &open_dat($chddat,'one');
    chomp $child;

    &get_uuser($hw);
    &name_title($usx,$sx);
    @icd = split(/,/,$cd);
    @ucd = split(/,/,$ucd);
    push(@icd,"$child（$unm）");
    push(@ucd,"$child（$nm）");
    $cd  = join(',',@icd);
    $ucd = join(',',@ucd);
    &msg("$unm$unt과의 아기가 태어났습니다. <br>신님이 $child의 이름을 붙여줬습니다");
    $babymsg = "$unm$unt과의 아기, $child(이/가) 태어났습니다";
    &add_record($babymsg);
    &add_record($babymsg,'other');
    $unw .= "$babymsg<br>";
    &add_news("$nm$int과 $unm$unt의 아기, $child(이/가) 태어났습니다");

    $t2  = time;
    undef $pg;
    &set_uuser if !$dead;
}

# Sub Love Match #
sub love_match {
    return 0 if !$_[0] || !$_[1];
    $count = $def_tv - 1,
    $totalpoint = 1;
    $I = $_[0];
    @U = split(/ */,$_[1]);
    foreach (1 .. $count + 1) { $totalpoint *= $_ }
    $point = $totalpoint;
    foreach $no (0 .. $count - 1) {
        $minus = 1;
        $bingo = index $I,$U[$no];
        $I =~ s/$U[$no]//;
        foreach (1 .. $count - $no) { $minus *= $_ }
        $point -= $minus * $bingo;
    }
    return $per = int($point / $totalpoint * 100);
}

# Sub Working #
sub working {
    $jiv = index($iv,'8');
    return if !$jb;
    ($jnm,$jss,$jpc,$jbn,$jlv,$jtm) = split(/,/,$jb);
    $jyr = int((time - $jtm) / ($def_yr * 60 * 60));
    srand($$ | time);
    foreach (1 .. $jyr) {
        &get_date($jtm + $_ * $def_yr * 60 * 60);
        if    ($sic) { &add_record("아퍼서 일을 쉬었습니다") }
        elsif ($pg)  { &add_record("출산휴가를 얻었습니다") }
        elsif (int(rand(100)) <= $jiv + $def_lj) { # 성실함 보너스
            &add_record("일을 농땡이 쳤습니다");
        }
        else {
            if (rand(100) <= $jpc && $jlv < $#JL) {
                $jlv++;
                &add_record("$JL[$jlv]$jnm(로/으로) 승격했습니다");
            }
            $pay = $jss + $jbn * $jlv;
            if (rand(100) <= $def_gj) {
                $pay *= $def_bp;
                $bonusrecord = '임시 보너스!!';
            }
            $mn += $pay;
            &add_record("$bonusrecord $pay G의 수입이 있었습니다");
            undef $bonusrecord;
        }
    }
    $jtm = $jtm + $jyr * $def_yr * 60 * 60;
    $jb = join(',',$jnm,$jss,$jpc,$jbn,$jlv,$jtm);
}

# Sub Face Check #
sub face_check {
    local($age) = &get_age($t1);
    if ($age >= $def_il) { $lfc = 0; $sic = 1; &msg("아픕니다") } # 일정기간 방치
    elsif ($blue)        { $lfc = 1   } # 쇼크일 때
    elsif ($shy)         { $lfc = 5   } # 사랑을 하고 있을 때
    else                 { $lfc = $fc } # 그 외
    $lfm = $sx ? $GF[$lfc] : $BF[$lfc];
    $lfc = $FL[$lfc];
    $lfc = $_[0] ? '자기소개가 있어요!' : $lfc;
    return qq|<td><img src=$img/$lfm alt="$lfc" width="$fce_wth" height="$fce_hgt"></td>\n|;
}

# Sub Job Check #
sub job_check {
    ($jnm,$jlv) = (split(/,/,$jb))[0,4] if $jb;
    $job = $pg ? "<b><font color=$tbl_lnc>임신중</font></b>" : $jb ? "$JL[$jlv]$jnm" : $def_jb;
}

# Sub Date Check #
sub date_check {
    ($elsline) = &open_dat($elsdat);
    ($eday,$emon) = split(/,/,$elsline);
    &get_date(time);
    $eday += $def_ag; # 연령이 1오르는 일수를 가산
    if    ($day   >  $eday)                   { &dead_check }
    elsif ($day == $eday && $hour >= $def_dh) { &dead_check }
    elsif ($month != $emon)                   { &dead_check }
}

# Sub Dead Check #
sub dead_check {
    &get_all_users;
    $number = $def_oa - $def_ya + 1; # 최고연령으로부터 최저연령을 찾는다
    foreach (@alllines) {
        $dead = $count = 0; undef $dice;
        ($aid,$anm,$aps,$aag,$abl,$at1)  = (split(/<>/))[0,1,2,9,14,31];
        next if &get_crypt($adps,$aps);
        srand($$ | time - $aag);
        next if $id eq $aid;
        local($age) = &get_age($aag);
        local($chr) = &get_age($at1);
        $dice = int(rand($number)) + $age;
        if    ($chr  >= $def_dd) { $dead = 1 } # 격려기한 초과
        elsif ($age  >  $def_oa) { $dead = 2 } # 최고사망연령 이상
        elsif ($age  <  $def_ya) { next      } # 최고사망연령 미만
        elsif ($dice >  $def_oa) { $dead = 2 } # 랜덤으로 수명을 결정
        if ($dead) {
            $count = split(/△/,$abl);
            &add_news("$anm(이/가) 사망했습니다. 조문객 = $count명") if $dead == 1;
            &add_news("$anm(이/가) 천수를 다했습니다. 조문객 = $count명") if $dead == 2;
            unlink("$usrdir/$aid\.dat");
        }
    }
    $elsline = join(',',$day,$month);
    &write_dat("$elsdat",$elsline);
}

# Sub IP Check #
sub ip_check {
    $X = $_[0]; $Y = $_[1];
    $X =~ s/(\d+)\.(\d+)\.(\d+)\.(\d+)/$1\.$2\.$3\./;
    $Y =~ s/(\d+)\.(\d+)\.(\d+)\.(\d+)/$1\.$2\.$3\./;
    if ($X eq $Y) { return 1 } else { return 0 }
}

# Sub Lover's Death #
sub lovers_death {
    $uid = $_[0];
    # 자신이 좋아하는 사람 리스트
    %ibl = map  { $_->[0] => [@$_] }
           map  { [split(/,/)] } split(/△/,$bl);

    # 자신의 연인 리스트
    %ilv = map  { $_->[0] => [@$_] }
           map  { [split(/,/)] } split(/△/,$lv);
    
    undef $hw if $hw eq $uid;
    $unm = $ibl{"$uid"}[1];
    delete $ibl{"$uid"};
    delete $ilv{"$uid"};
    @bl  = sort map { join(',',@$_) } values %ibl;
    $bl  = join('△',@bl);
    @lv  = sort map { join(',',@$_) } values %ilv;
    $lv  = join('△',@lv);
    
    &msg("$unm(이/가) 사망했습니다. $nm(은/는) 슬픔에 잠겨 있습니다.");
    &add_record("$unm(이/가) 사망했습니다. $nm(은/는) 슬픔에 잠겨 있습니다.");
    $blue = $fc = $dead = 1;
}

# Sub I Profile #
sub iprofile {
    $age = &get_age($ag);
    $face = &face_check;
    @ilv = sort { $b->[3] <=> $a->[3] }
           map  { [split(/,/)] } split(/△/,$lv);
    $lno = @ilv;
    &job_check;
    @ft = split(/,/,$ft);
    $cdn = @cd = split(/,/,$cd);
    $petname = $pnm ? $pnm : "애완동물";

    print qq|<table border=0 cellspacing=0 cellpadding=1 width=100%>\n|;
    if ($def_ic && $ci) {
        print qq|<tr><td rowspan=4 align=center width=$def_is><img src=$img/$ci><br>$nm</td>\n|;
        print qq|$face</tr>\n|;
        print qq|<tr><td>나이：$age세</td></tr>\n|;
        print qq|<tr><td>$mny_img：$mn G</td></tr>\n|;
        print qq|<tr><td>직업：$job</td></tr>\n|;
    }
    else {
        print qq|<tr><td>이름：$nm</td>$face</tr>\n|;
        print qq|<tr><td>나이：$age세</td><td>$mny_img：$mn G</td></tr>\n|;
        print qq|<tr><td colspan=2>직업：$job</td></tr>\n|;
    }
    print qq|</table>\n|;

    print qq|<br>\n|;
    if ($msg eq '') { &msg("$FL[$fc]") }
    print qq|$msg|;
    print qq|<br><br>\n|;
    print qq|차인 회수：$rn<br>\n|;
    print qq|지금까지 사귄 수：$ln<br>\n|;
    print qq|연인의 수：$lno<br>\n|;
    foreach (@ilv) {
        ($uid,$usx,$unm,$ulp) = @$_;
        $mp = $uid eq $hw ? " [$MP[$sx]]" : '';
        &name_title($usx);
        $on_click = qq|onClick="return opWin('$cgiurl?mode=uprofile&id=$uid','win5')"|;
        print qq|　 <a href="$cgiurl?mode=uprofile&id=$uid" $on_click target=_blank>$unm$unt$mp</a><br>\n|;
    }
    print qq|아이의 수：$cdn<br>\n|;
    foreach (@cd) { print qq|　 $_<br>\n| };
    print qq|<br>\n|;
    print qq|재산：\n|;
    foreach (@ft) {
        ($ftn,$fti) = split(/△/);
        print qq|<img src="$img/$fti" alt="$ftn">\n|;
    }
    print qq|<br>\n|;
    print qq|선물：\n|;
    print qq|$prz_img\n| x $pr;
    print qq|<hr class=text>\n|;
    print qq|$petname의 먹이：\n|;
    print qq|$pfd_img\n| x $pfd;
    print qq|<br>|;
    print qq|$petname：\n|;
    print qq|<img src="$img/$pim" alt="$in" width="$pet_wth" height="$pet_hgt">\n| if $pim;
    print qq|<br>$petname 일기：$pmsg\n| if $pmsg;
#    print qq|<hr class=text>\n| if $in;
#    print qq|$in\n| if $in;
}

# Sub U Profile #
sub uprofile {
    &get_iuser($F{'id'});
    $age = &get_age($ag);
    $face = &face_check;
    @ilv = sort { $b->[3] <=> $a->[3] }
           map  { [split(/,/)] } split(/△/,$lv);
    $lno = @ilv;
    &job_check;
    @ft = split(/,/,$ft);
    $cdn = @cd = split(/,/,$cd);
    $petname = $pnm ? $pnm : "애완동물";
    if ($ml) { $ml = "<a href=mailto:$ml>$mel_img</a>" }
    if ($ul) { $ul = "<a href=$ul target=_blank>$url_img</a>" }

    &header;
    &first_box('up');
    &second_box('up','form');
    &title;
    print qq|<table border=0 cellspacing=0 cellpadding=1 width=100%>\n|;
    if ($def_ic && $ci) {
        print qq|<tr><td rowspan=5 align=center width=$def_is><img src=$img/$ci><br>$nm</td>\n|;
        print qq|$face</tr>\n|;
        print qq|<tr><td>나이：$age세</td></tr>\n|;
        print qq|<tr><td>$mny_img：$mn G</td></tr>\n|;
        print qq|<tr><td>직업：$job</td></tr>\n|;
        print qq|<tr><td>$ml $ul</td></tr>\n|;
    }
    else {
        print qq|<tr><td>이름：$nm $ml $ul</td>$face</tr>\n|;
        print qq|<tr><td>나이：$age세</td><td>$mny_img：$mn G</td></tr>\n|;
        print qq|<tr><td colspan=2>직업：$job</td></tr>\n|;
    }
    print qq|</table>\n|;

    print qq|<br>\n|;
    print qq|차인 회수：$rn<br>\n|;
    print qq|지금까지 사귄 수：$ln<br>\n|;
    print qq|연인의 수：$lno<br>\n|;
    foreach (@ilv) {
        ($uid,$usx,$unm,$ulp) = @$_;
        $mp = $uid eq $hw ? " [$MP[$sx]]" : '';
        &name_title($usx);
        print qq|　 <a href="$cgiurl?mode=uprofile&id=$uid&return=1">$unm$unt$mp</a><br>\n|;
    }
    print qq|아이의 수：$cdn<br>\n|;
    foreach (@cd) { print qq|　 $_<br>\n| };
    print qq|<br>\n|;
    print qq|재산：\n|;
    foreach (@ft) {
        ($ftn,$fti) = split(/△/);
        print qq|<img src="$img/$fti" alt="$ftn">\n|;
    }
    print qq|<br>\n|;
    print qq|선물：\n|;
    print qq|$prz_img\n| x $pr;
    print qq|<hr class=text>\n|;
    print qq|$petname의 먹이：\n|;
    print qq|$pfd_img\n| x $pfd;
    print qq|<br>|;
    print qq|$petname：\n|;
    print qq|<img src="$img/$pim" width="$pet_wth" height="$pet_hgt">\n| if $pim;
    print qq|<hr class=text>\n| if $in;
    print qq|<b>$in</b>\n| if $in;
    print qq|<br><br>\n|;
    &return_button("player_list",'','button') if $F{'return'};
    &second_box('down');
    &first_box('down');
    &footer('nocopyright');
}

# Sub Player List #
sub player_list {
    &header;
    &first_box('up','smallwindow');
    &second_box('up','form');
    &title;

    print qq|<a href=$cgiurl?mode=player_list&sort=0>[ID순]</a>\n|;
    print qq|<a href=$cgiurl?mode=player_list&sort=1>[이름순]</a>\n|;
    print qq|<a href=$cgiurl?mode=player_list&sort=10>[소지금순]</a>\n|;
    print qq|<a href=$cgiurl?mode=player_list&sort=16>[연애왕]</a>\n|;
    print qq|<a href=$cgiurl?mode=player_list&sort=17>[실연왕]</a>\n|;
    print qq|<a href=$cgiurl?mode=player_list&sort=35>[재산왕]</a>\n|;
    &get_all_users;
    $st = $F{'sort'};
    $lbl = $st == 16 ? '연애왕' :
           $st == 17 ? '실연왕' :
           $st == 35 ? '재산왕' :
                       '거주자 일람';

    if    ($st == 0) {
        @alllines = map  { $_->[0] }
                    sort { $a->[1] <=> $b->[1] }
                    map  { [$_,(split(/<>/))[$st]] } @alllines;
    }
    elsif ($st == 1) {
        @alllines = map  { $_->[0] }
                    sort { $a->[1] cmp $b->[1] }
                    map  { [$_,(split(/<>/))[$st]] } @alllines;
    }
    else {
        @alllines = map  { $_->[0] }
                    sort { $b->[1] <=> $a->[1] }
                    map  { [$_,(split(/<>/))[$st]] } @alllines;
    }

    &page($F{'pg'},$#alllines,$def_pj);
    print qq|<b><a href=$cgiurl?mode=player_list&pg=$back&sort=$st>[앞]</a></b>| if $back >= 0;
    print qq|<b><a href=$cgiurl?mode=player_list&pg=$next&sort=$st>[뒤]</a></b>| if $end != $total;

    for ($i=0; $i <= $#alllines; $i += $def_pj) {
        $pge_nm = $i / $def_pj + 1;
        $tag = $i == $F{'pg'} ? "[$pge_nm]" : "<a href=$cgiurl?mode=player_list&pg=$i&sort=$st>[$pge_nm]</a>";
        print qq|<b>$tag</b>|;
    }

    print qq|<br><br>\n|;
    &label($lbl);

    print qq|<table align=center width=100%>\n|;
    foreach ($start .. $end) {
        ($id,$nm,$sx,$jb,$fc,$ag,$mn,$lv,$pt,$in,$t1,$pg,$xx) = 
        (split(/<>/,$alllines[$_]))[0,1,3,6,8,9,10,18,24,29,31,33,$st];
        ($pnm,$pim,$pfd,$ptm,$pdt) = split(/,/,$pt);
        $pet = $pim ? qq|<img src=$img/$pim alt="$pnm" width="$pet_wth" height="$pet_hgt">| : '';
        $lvs = '';
        @ilv = sort { $b->[3] <=> $a->[3] }
               map  { [split(/,/)] } split(/△/,$lv);
        foreach (@ilv) {
            $sex_img = $_->[1] ? 'woman.gif' : 'man.gif';
            $lvs .= qq|<img src=$img/$sex_img alt="$_->[2]" width="$sex_wth" height="$sex_hgt">|;
        }
        &job_check;
        $face = &face_check($in);
        $age  = &get_age($ag);
        print qq|<tr>\n|;
        print qq|<td><a href=$cgiurl?mode=uprofile&id=$id&return=1>$nm</a></td>\n|;
        print $face;
        print qq|<td align=right nowrap>$age세</td>\n|;
        print qq|<td>$pet</td>\n|;
        print qq|<td>$lvs</td>\n|;
        print qq|<td nowrap>$job</td>\n|;
        if ($st == 17 || $st == 16) { $lbl = "$xx 회" }
        elsif ($st == 35)           { $lbl = "$xx G"  }
        else                        { $lbl = "$mn G"  }
        print qq|<td align=right nowrap>$lbl</td>\n|;
        print qq|</tr>\n|;
    }
    print qq|</table>\n|;
    &second_box('down');
    &first_box('down');
    &footer('nocopyright');
}

# Sub ID List #
sub id_list {
    &header;
    &first_box('up');
    &second_box('up','form');
    &title;
    &get_all_users;
    print qq|<table align=center>\n|;
    foreach (@alllines) {
        ($id,$nm,$sx) = (split(/<>/))[0,1,3];
        $sex_img = $sx ? $wmn_img : $man_img;
        print qq|<tr><td>$id</td><td>$sex_img</td><td>$nm</td></tr>|;
    }
    print qq|</table>\n|;
    &second_box('down');
    &first_box('down');
    &footer('nocopyright');
}

# Sub Page #
sub page {
    ($first,$total,$eachpage) = @_;
    $start = $first eq '' ? 0 : $first;
    $end   = $start + ($eachpage - 1);
    $end   = $total if $end >= $total;
    $next  = $end + 1;
    $back  = $start - $eachpage;
}

# Sub History #
sub history {
    &header;
    &first_box('up','smallwindow');
    &second_box('up','form');
    &title;
    &label('이력');
    &get_iuser($F{'id'});
    foreach (@ilines) { print "$_<br>\n" }
    &second_box('down');
    &first_box('down');
    &footer('nocopyright');
}

# Sub news #
sub news {
    &header;
    &first_box('up','smallwindow');
    &second_box('up','form');
    &title;
    &label('거주자 뉴스');
    @newslines = &open_dat($nwsdat);
    foreach (@newslines) { print "$_<br>\n" }
    &second_box('down');
    &first_box('down');
    &footer('nocopyright');
}

# Sub Header #
sub header {
    print qq|Content-type: text/html\n\n|;
    print qq|<html>\n<head>\n|;
    print qq|<meta http-equiv="Content-Type" content="text/html; charset=euc_kr">\n|;
    print qq|<title>$title</title>\n|;
    if ($def_st) { print qq|<link rel="stylesheet" href="$def_su" type="text/css">\n| }
    else { &style }
    &java_script if $_[0];
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
        print qq|<br><center><font color="$tbl_lnc">PeoPle Ver $ver<br>\n|;
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
    print qq|A:link    { text-decoration:none;color:$nlc_clr;font-weight:bold }\n|;
    print qq|A:visited { text-decoration:none;color:$vlc_clr;font-weight:bold }\n|;
    print qq|A:hover   { text-decoration:none;color:$alc_clr;font-weight:bold }\n|;
    print qq|body,tr,td,th { font-size:$fnt_sze }\n|;
    print qq|.button { font-size:$but_sze;border:solid;border-width:3pt 1pt;border-color:$tbl_lnc;background-color:$txb_clr }\n|;
    print qq|.text   { font-size:$txb_sze;border:solid;overflow:visible;border-width:1pt;border-color:$tbl_lnc;background-color:$txb_clr }\n|;
    print qq|-->\n|;
    print qq|</STYLE>\n|;
}

# Java Script
sub java_script {
    print qq|<SCRIPT LANGUAGE="JavaScript">\n|;
    print qq|<!--\n|;
    print qq|var w = window;\n|;
    print qq|function opWin(url,wname){\n|;
    print "if ((w == window) || w.closed) {\n";
    print qq|       w = open(url,wname,"scrollbars=yes,resizable=yes,width=$smw_wth,height=$smw_hgt");\n|;
    print qq|   } else {\n|;
    print qq|       w.location.replace(url);\n|;
    print qq|       w.focus();\n|;
    print qq|   }\n|;
    print qq|   return(false);\n|;
    print qq|}\n|;
    print qq|//-->\n|;
    print qq|</SCRIPT>\n|;
}

# Sub First Box #
sub first_box {
    if ($_[1]) { $dz_bw = $stb_wth } else { $dz_bw = $mtb_wth }
    if    ($_[0] eq 'up')   {
        print qq|<div align=center>\n|;
        print qq|<table border=0 cellspacing=0 cellpadding=0 bgcolor=$tbl_bgc width=$dz_bw>\n|;
        print qq|<tr>\n|;
        print qq|<td><img src=$img/lt.gif width=8 height=8></td>\n|;
        print qq|<td><img src=$img/1p.gif></td>\n|;
        print qq|<td align=right><img src=$img/rt.gif width=8 height=8></td>\n|;
        print qq|</tr>\n|;
        print qq|<tr>\n|;
        print qq|<td><img src=$img/1p.gif></td>\n|;
        print qq|<td>\n|;
    }
    elsif ($_[0] eq 'down') {
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
    if    ($_[0] eq 'up')     {
        print qq|<table border=1 cellspacing=0 cellpadding=5 width=100% bordercolorlight=$tbl_lnc bordercolordark=$tbl_lnc bordercolor=$tbl_lnc>\n|;
        print qq|<tr>\n|;
        print qq|<form method=$method action=$cgiurl>\n| if $_[1];
        print qq|<td>\n|;
    }
    elsif ($_[0] eq 'middle') {
        print qq|</td>\n|;
        print qq|</tr>\n|;
        print qq|<form method=$method action=$cgiurl>\n|;
        print qq|<tr>\n|;
        print qq|<td>\n|;
    }
    elsif ($_[0] eq 'down')   {
        print qq|</td>\n|;
        print qq|</tr>\n|;
        print qq|</form>\n|;
        print qq|</table>\n|;
    }
}

# Sub Action Select #
sub action_select {
    print qq|<input type="radio" name="mode" value="cheer" checked>격려한다\n|;
    print qq|<input type="radio" name="mode" value="shopping">쇼핑\n|;
    print qq|<input type="radio" name="mode" value="new_job">전직\n|;
    print qq|<br>\n|;
    print qq|<input type="radio" name="mode" value="introduce">소개문\n|;
    print qq|<input type="radio" name="mode" value="mail_form">메일\n| if $fb =~ /Ca/ && $fb =~ /Cb/ && $def_ml;
    print qq|<br><input type="radio" name="mode" value="pet_name">애완동물에게 이름을 붙인다\n| if !$pnm && $pim;
    print qq|<br><input type="radio" name="mode" value="select_icon">아이콘을 선택한다\n| if !$ci && $def_ic;
    &id_ps;
}

# Sub Title #
sub title {
    return if !$def_ti;
    print qq|<p align=center><img src=$img/$ttl_img width=$ttl_wth height=$ttl_hgt></p>\n|;
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

# Name Title #
sub name_title {
    $unt = $_[0] ? '양' : '군';
    $int = $_[1] ? '양' : '군';
}

# Sub ID & Password #
sub id_ps {
    print qq|<input type=hidden name=id value="$F{'id'}">\n|;
    print qq|<input type=hidden name=ps value="$F{'ps'}">\n|;
}

# Sub Submit Button #
sub submit_button {
    print qq|<br>\n|;
    print qq|<div align=right>\n|;
    print qq|<input type=submit value="$sub_lbl" class=button>\n|;
    print qq|</div>\n|;
}

# Sub Info Button #
sub info_button {
    $on_click = qq|onClick="return opWin('$cgiurl?mode=how_to_play','win1')"|;
    print qq|<a href=$cgiurl?mode=how_to_play $on_click target=_blank>설명서</a><br>\n|;
    print qq|<br>\n|;
}

# Sub Virtue Button #
sub virtue_button {
    $on_click = qq|onClick="return opWin('$cgiurl?mode=info_virtue','win7')"|;
    print qq|<a href=$cgiurl?mode=info_virtue $on_click target=_blank>덕목의 설명</a><br>\n|;
    print qq|<br>\n|;
}

# Sub New Regist Button #
sub new_regist_button {
    print qq|<a href=$cgiurl?mode=new_regist>신규등록</a><br>\n|;
    print qq|<br>\n|;
}

# Sub Player List Button #
sub player_list_button {
    $on_click = qq|onClick="return opWin('$cgiurl?mode=player_list','win2')"|;
    print qq|<a href=$cgiurl?mode=player_list $on_click target=_blank>[거주자 일람]</a>\n|;
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

# Sub History Button #
sub history_button {
    $on_click = qq|onClick="return opWin('$cgiurl?mode=history&id=$id&ps=$F{'ps'}','win3')"|;
    print qq|<a href=$cgiurl?mode=history&id=$id&ps=$F{'ps'} $on_click target=_blank>[이력]</a>\n|;
}

# Sub News Button #
sub news_button {
    $on_click = qq|onClick="return opWin('$cgiurl?mode=news&id=$id&ps=$F{'ps'}','win8')"|;
    print qq|<a href=$cgiurl?mode=news $on_click target=_blank>[거주자 뉴스]</a>\n|;
}

# Sub Add Record #
sub add_record {
    &get_date(time) if !$date;
    if ($_[1] && $_[0]) {
        $words =  "[$date] $_[0]\n";
        pop (@ulines) if @ulines >= $def_om;
        unshift (@ulines,$words);
    }
    elsif ($_[0]) {
        $words =  "[$date] $_[0]\n";
        pop (@ilines) if @ilines >= $def_om;
        unshift (@ilines,$words);
    }
}

# Sub Add_News #
sub add_news {
    &get_date(time) if !$date;
    unshift(@newslines,"[$date] $_[0]\n");
}

# Sub Write_News #
sub write_news {
    @newslines = (@newslines,&open_dat($nwsdat));
    while (@newslines > $def_nx) { pop @newslines }
    &write_dat("$nwsdat",@newslines);
    undef @newslines;
}

# Sub Message #
sub msg {
    return if !$_[0];
    $msg .= "<br>" if $msg;
    $msg .= "$_[0]\n";
}

# Sub Pet Message #
sub pet_msg {
    return if !$_[0];
    $pmsg .= "$_[0]\n";
}

# Sub Get Age #
sub get_age {
    $now  = time;
    $then = $_[0];
    $data = int(($now - $then) / ($def_ag * 60 * 60 * 24));
    return $data;
}

# Sub Get Date #
sub get_date {
    ($sec,$min,$hour,$day,$month,$year) = localtime($_[0]);
    $year += 1900;
    $month++;
    $date   = sprintf("%04d\/%02d\/%02d",$year,$month,$day);
}

# Sub Get I User #
sub get_iuser {
    return if $getiuserflag;
    open(IN,"$usrdir\/$_[0]\.dat") || &no_id($_[0]);
    @ilines = <IN>;
    close(IN);
    if (!@ilines) { &error("ID $_[0] 읽기 에러") }
    $userline = shift(@ilines);
    ($id,$nm,$ps,$sx,$ml,$ul,$jb,$lp,$fc,$ag,$mn,
     $ft,$pr,$nw,$bl,$cd,$ln,$rn,$lv,$iv,$uv,$af,
     $ac,$bs,$pt,$ht,$bz,$os,$fl,$in,$ci,$t1,$t2,
     $pg,$fb,$fp,$hw,$rr,$ap) = split(/<>/,$userline);
    ($pnm,$pim,$pfd,$ptm,$pdt) = split(/,/,$pt);
    if ($F{'ps'} eq $adps)        { $error = 1 }
    if (&get_crypt($F{'ps'},$ps)) { $error = 1 }
    if ($F{'mode'} eq 'uprofile') { $error = 1 }
    &error("패스워드가 틀립니다") if !$error;
    $getiuserflag = 1;
}

# Sub Get U User #
sub get_uuser {
    open(IN,"$usrdir\/$_[0]\.dat") || &lovers_death("$_[0]");
    @ulines = <IN>;
    close(IN);
    return(0) if $dead;
    $userline = shift(@ulines);
    ($uid,$unm,$ups,$usx,$uml,$uul,$ujb,$ulp,$ufc,$uag,$umn,
     $uft,$upr,$unw,$ubl,$ucd,$uln,$urn,$ulv,$uiv,$uuv,$uaf,
     $uac,$ubs,$upt,$uht,$ubz,$uos,$ufl,$uin,$uci,$ut1,$ut2,
     $upg,$ufb,$ufp,$uhw,$urr,$uap) = split(/<>/,$userline);
    return(1);
}

# Sub Get All Users #
sub get_all_users {
    return if $getallusersflag;
    opendir(DIR,"$usrdir") || &error("유저 데이터 읽기 에러 : $usrdir (라는/이라는) 이름의 유저 데이터용 디렉토리가 없거나 퍼미션이 틀립니다");
    @userfiles = sort grep /\.dat/,readdir(DIR);
    closedir(DIR);
    foreach (@userfiles) {
        open(IN,"$usrdir\/$_") || &error("$usrdir\/$_를 열 수 없습니다");
        ($line) = <IN>;
        push(@alllines,$line);
        close(IN);
    }
    $getallusersflag = 1;
}

# Sub Set I User #
sub set_iuser {
    $pt   = join(',',$pnm,$pim,$pfd,$ptm,$pdt);
    $line = join('<>',$id,$nm,$ps,$sx,$ml,$ul,$jb,$lp,$fc,$ag,$mn,
                      $ft,$pr,$nw,$bl,$cd,$ln,$rn,$lv,$iv,$uv,$af,
                      $ac,$bs,$pt,$ht,$bz,$os,$fl,$in,$ci,$t1,$t2,
                      $pg,$fb,$fp,$hw,$rr,$ap,"\n");
    unshift (@ilines,$line);
    &error("쓰기 에러(I)") if !$id;
    &write_dat("$usrdir\/$id\.dat",@ilines);
}

# Sub Set U User #
sub set_uuser {
    $line = join('<>',$uid,$unm,$ups,$usx,$uml,$uul,$ujb,$ulp,$ufc,$uag,$umn,
                      $uft,$upr,$unw,$ubl,$ucd,$uln,$urn,$ulv,$uiv,$uuv,$uaf,
                      $uac,$ubs,$upt,$uht,$ubz,$uos,$ufl,$uin,$uci,$ut1,$ut2,
                      $upg,$ufb,$ufp,$uhw,$urr,$uap,"\n");
    unshift (@ulines,join('<>',$line));
    &error("쓰기 에러(U)") if !$uid;
    &write_dat("$usrdir\/$uid\.dat",@ulines);
}

# Sub No ID #
sub no_id {
    &get_all_users;
    ($idcheck)   = map  { $_->[0] }
                   sort { $b->[0] <=> $a->[0] }
                   map  { [(split(/<>/))[0]] } @alllines;
    if (!$_[0]) { &error("ID가 없습니다") }
    elsif ($idcheck > $_[0]) { &error("그 ID의 주인은 사망했거나 존재하지 않습니다") }
    else { &error("그 ID의 플레이어는 존재하지 않습니다") }
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
    $c_id = $COOKIE{'id'};
    $c_ps = $COOKIE{'ps'};
}

# Sub Set Cookie #
sub set_cookie {
    # 쿠키는 90일간 유효　
    ($secg,$ming,$hourg,$mdayg,$mong,$yearg,$wdayg,$ydayg,$isdstg) = gmtime(time + 90*24*60*60);
    $yearg += 1900;
    if ($secg  < 10) { $secg  = "0$secg";  }
    if ($ming  < 10) { $ming  = "0$ming";  }
    if ($hourg < 10) { $hourg = "0$hourg"; }
    if ($mdayg < 10) { $mdayg = "0$mdayg"; }
    $month = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')[$mong];
    $youbi = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')[$wdayg];
    $date_gmt = "$youbi, $mdayg\-$month\-$yearg $hourg:$ming:$secg GMT";
    $cook = "id\:$F{'id'}\,ps\:$F{'ps'}";
    print "Set-Cookie: $cookname=$cook; expires=$date_gmt\n";
}

# Sub Get Host #
sub get_host {
    $ht = $ENV{'REMOTE_HOST'};
    $ad = $ENV{'REMOTE_ADDR'};
    if ($get_remotehost) {
        if ($ht eq "" || $ht eq "$ad") {
            $ht = gethostbyaddr(pack("C4",split(/\./,$ad)),2);
        }
    }
    if ($ht eq "") { $ht = $ad }
}

# Sub Get Agent #
sub get_agent {
    $bz = $os = $ENV{'HTTP_USER_AGENT'};

    $_ = $bz;
    $bz = /MSIE 3/i         ? 'MSIE 3':
          /MSIE 4/i         ? 'MSIE 4':
          /MSIE 5/i         ? 'MSIE 5':
          /MSIE 6/i         ? 'MSIE 6':
          /MSIE 7/i         ? 'MSIE 7':
          /MSIE 8/i         ? 'MSIE 8':
          /Mozilla\/2/i     ? 'Netscape 2':
          /Mozilla\/3/i     ? 'Netscape 3':
          /Mozilla\/4/i     ? 'Netscape 4':
          /Mozilla\/5/i     ? 'Netscape 5':
          /Netscape ?6/i    ? 'Netscape 6':
          /Netscape ?7/i    ? 'Netscape 7':
          /Netscape ?8/i    ? 'Netscape 8':
          /AOL/             ? 'AOL':
          /Opera/i          ? 'Opera':
          /Lynx/i           ? 'Lynx':
          /Cuam/i           ? 'Cuam':
          /DoCoMo/i         ? 'i-mode':
          /J-PHONE/i        ? 'J-Skyweb':
          /Internet Ninja/i ? 'Internet Ninja':
                              'Unknown Browser';
    $_ = $os;
    $os = /Windows 95/i      || /Win95/i      ? 'Win95':
          /Windows 9x/i      || /Win 9x/i     ? 'WinMe':
          /Windows 98/i      || /Win98/i      ? 'Win98':
          /Windows XP/i      || /WinXP/i      ? 'WinXP':
          /Windows NT 5\.1/i || /WinNT 5\.1/i ? 'WinXP':
          /Windows NT 5/i    || /WinNT 5/i    ? 'Win2000':
          /Windows 2000/i    || /Win2000/i    ? 'Win2000':
          /Windows NT/i      || /WinNT/i      ? 'WinNT':
          /Windows CE/i      || /WinCE/i      ? 'WinCE':
          /Mac/i                              ? 'Mac':
          /sharp pda browser/i                ? 'ZAURUS':
          /X/                ||
          /Sun/i             ||
          /Linux/i           ||
          /HP-UX/i           ||
          /OSF1/i            ||
          /IRIX/i            ||
          /BSD/i                              ? 'UNIX':
                                                'Unknown Os';
}

# Sub Get Cryptogram #
sub get_crypt {
    $word  = $_[0];
    $crypt = $_[1];
    if (!$def_cp) { if ($word eq $crypt) { return 1 } else { return 0 } }
    $salt  = substr($crypt,0,2);
    if ($crypt eq crypt($word,$salt))    { return 1 } else { return 0 }
}

# Sub Set Cryptogram #
sub set_crypt {
    $word = $_[0];
    return $word if !$def_cp;
    srand($$ | time);
    $xx = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        . "abcdefghijklmnopqrstuvwxyz"
        . "0123456789./";
    $salt  = substr($xx,int(rand(64)),1);
    $salt .= substr($xx,int(rand(64)),1);
    return $crypt = crypt($word,$salt);
}

# Sub Open Dat #
sub open_dat {
local (@lines,$line);
    open(IN,"$_[0]") || &error("$_[0]읽기 에러:$_[0]가 존재하지 않거나 퍼미션이 부정확합니다");
    if ($_[1]) { rand($.) < 1 and $line = $_ while <IN> }
    else       { @lines = <IN> }
    close(IN);
    return $_[1] ? $line : @lines;
}

# Sub Write Dat #
sub write_dat {
    open(OUT,">$_[0]") || &error("$_[0]쓰기 에러:$_[0]가 존재하지 않거나 퍼미션이 부정확합니다");
    shift(@_);
    print OUT @_;
    close(OUT);
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
    &return_button('','','button') if !$def_rb;
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
            --$flag or &error('현제, 서버가 혼잡합니다',1);
            sleep(1);
        }
    }
    elsif ($lockkey == 2) {
        unlink($lockfile) if (time - (stat($lockfile))[9] > 60);
        while (!symlink(".",$lockfile)) {
            --$flag or &error('현제, 서버가 혼잡합니다',1);
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
        $value =~ s/\,/,/g;
        $value =~ s/\r\n/<br>/g;
        $value =~ s/\r/<br>/g;
        $value =~ s/\n/<br>/g;

        $F{$name} = $value;
    }
}
# ######################### 서브 루틴 종료 #########################
