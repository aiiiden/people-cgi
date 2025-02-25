## PeoPle

PeoPle은 여러 사람이 참가하는 연애형식의 게임입니다. 당신을 닮은 분신을 웹에 생성하여 생활시킵니다. 한번 생성한 주민은 이후 자율적으로 다른 주민과 연애를 합니다. 주민은 자신이 좋아하는 사람에게 접근하여 애인이 되려고 합니다. 때로는 싸우거나, 헤어지거나, 데이트하거나, 선물을 주고받거나, 죽거나, 결혼하여 자녀를 낳기도 합니다. 또한 일을 통해 수입을 얻어 그 돈으로 애완동물을 기르거나 아이템(재산)을 구매할 수 있습니다.

PeoPle is a dating-style game where multiple people participate. You create an avatar that resembles you on the web and let it live. Once created, the residents autonomously interact and date other residents. Residents approach people they like and try to become their partners. Sometimes they fight, break up, go on dates, exchange gifts, die, get married, and have children. They can also earn income through work and use that money to raise pets or buy items (assets).

## 파일 설명 / File Description

- `people.cgi` : PeoPle본체의 CGI입니다. / The main CGI of PeoPle.
- `new.cgi` : PeoPle의 서브프로그램 / A subprogram of PeoPle.
- `lovers.cgi` : PeoPle의 서브프로그램 / A subprogram of PeoPle.
- `admin.cgi` : 관리자용의 CGI입니다. / The administrator CGI.
- `itm.dat` : 구입가능한 아이템리스트입니다. / List of purchasable items.
- `job.dat` : 직업 리스트입니다. / List of jobs.
- `chd.dat` : 자식 리스트입니다. / List of children.
- `pzt.dat` : 선물 리스트입니다. / List of gifts.
- `dte.dat` : 데이트장소 리스트입니다. / List of date places.
- `els.dat` : 그외의 데이터를 보관합니다. / Stores other data.
- `pet.dat` : 펫의 일기가 들어있습니다. / Contains the diary of the pet.
- `htp.dat` : 놀이방법의 설명이 들어있습니다. / Contains the description of how to play.
- `vti.dat` : 캐릭터작성의 설명이 들어있습니다. / Contains the description of character creation.
- `vtd.dat` : 8덕의 설명이 들어있습니다. / Explanation of the 8 virtues.
- `nws.dat` : 주민뉴스를 보관합니다. / Stores resident news.
- `img폴더` : 이미지 파일이 들어있습니다. / Contains image files.
- `index.html` : 더미용 HTML파일 / Dummy HTML file.

## 퍼미션 설정 / Permission Setting

FTP소프트등을 이용해 파일의 퍼미션을 변경해주세요.
Please change the file permissions using FTP software, etc.

- `people.cgi` : 755(or 705)
- `admin.cgi` : 755(or 705)
- `mppl.cgi` : 755(or 705)
- `new.cgi` : 644
- `lovers.cgi` : 644
- `모든dat` : 666(or 606)
  ※ 보관하는 폴더는 777(또는 707)로 해주세요(유저데이터 포함) / The folder where these files are stored should be set to 777 (or 707) (including user data).

## 디렉토리 구성 / Directory Layout

디렉토리의 샘플배열입니다.
Sample directory layout:

```
 public_html┬index.html
            └people┬img : 이미지 / Images
                    ├ 유저 데이터(※1) / User data(※1)
                    ├ people.cgi(755)
                    ├ new.cgi(644)
                    ├ lovers.cgi(644)
                    ├ admin.cgi(755)
                    ├ mppl.cgi(755)
                    ├ index.html(※2)
                    ├ itm.dat
                    ├ job.dat
                    ├ chd.dat
                    ├ pzt.dat
                    ├ dte.dat
                    ├ els.dat
                    ├ pet.dat
                    ├ htp.dat
                    ├ vti.dat
                    ├ vtd.dat
                    └ nws.dat
```

1. 유저 데이터를 보관하기 위해 디렉토리(폴더)를 생성합니다. 알파벳으로 임의의 이름을 붙입니다. 그 후, people.cgi와 admin.cgi를 텍스트 편집기로 열어 34번째 줄의 이름을 해당 폴더명으로 변경합니다. 초기값은 「userdata」로 되어 있지만, 보안을 위해 반드시 변경해주세요. 유저 데이터용 디렉토리의 퍼미션은 777(또는 707)로 설정해주세요. / Create a directory to store user data. Assign an arbitrary name in the alphabet. Then open people.cgi and admin.cgi with a text editor and change the name to the folder name on the 34th line. The initial value is "userdata", but please change it for security. Set the permission of the user data directory to 777 (or 707).

2. 외부로부터 내용이 보여질 우려가 있을 경우, 더미용 index.html을 함께 업로드해주세요. FTP 소프트웨어 등을 사용해 서버에 전송합니다. / If there is a concern that the content may be visible from the outside, please upload a dummy index.html. Transfer it to the server using FTP software, etc.

3. 이미지는 하나로 묶어 임의의 폴더 안에 넣어주세요. 이미지 폴더를 두는 위치는 어디든 상관없습니다. 또한 폴더명도 임의로 지정해도 괜찮습니다. / Put the images in one folder. The location of the image folder does not matter. You can also specify the folder name arbitrarily.

## 프로그램의 수정 / Modification of the Program

people.cgi, admin.cgi는 이대로 사용할 수 없습니다. 각 프로바이더나 디렉토리 구성에 따라 변경할 필요가 있습니다. people.cgi, admin.cgi를 텍스트 문자편집기 등으로 열어, 이하의 개소를 변경해주세요.
※ lovers.cgi와 new.cgi는 변경할 필요가 없습니다.

people.cgi and admin.cgi cannot be used as they are. Depending on the provider or directory configuration, changes may be necessary. Open people.cgi and admin.cgi with a text editor, such as a text editor, and change the following items.
※ There is no need to change lovers.cgi and new.cgi.

```perl
#!/usr/bin/perl
```

프로바이더에 정해진 Perl로의 패스를 지정합니다. 대부분의 경우 #!/usr/bin/perl 혹은 #!/usr/local/bin/perl 입니다.

Specify the path to Perl defined by the provider. In most cases, it is #!/usr/bin/perl or #!/usr/local/bin/perl.

```perl
$usrdir = 'userdata';
```

유저데이터를 보관하는 디렉토리(폴더)입니다. 초기치는 userdata라고 되어있지만, 반드시 변경해주세요. 그 후, 서버에 동명의 디렉토리(폴더)를 전송하거나 작성해서, 퍼미션을 777(707)로 합니다.

The directory that stores user data. The initial value is "userdata", but please change it. Then transfer or create a directory with the same name on the server and set the permission to 777 (707).

```perl
$img = '/img';
```

이미지 디렉토리(폴더)를 CGI와 같은 위치에 둘 수 있는 경우 그대로 사용합니다. 가능 여부는 서비스 제공자(서버)에 따라 다릅니다. 불확실한 경우 서비스 제공자(서버)에 문의해주세요. 불가능한 경우, cgi-bin 상위 디렉토리에 이미지 폴더를 위치시켜야 합니다. 이 경우 설치한 이미지 디렉토리에 맞게 경로를 변경해야하므로, 자신의 경로에 맞춰 이 부분을 수정합니다. 상대 경로와 절대 경로 모두 사용 가능합니다.

If you can place the image directory in the same location as the CGI, use it as it is. Whether this is possible depends on the service provider (server). If you are unsure, please contact the service provider (server). If it is not possible, the image folder must be located in the directory above cgi-bin. In this case, you need to change this part according to the installed image directory, so modify it according to your path. Both relative and absolute paths are possible.

example 1: `$img = '../../img';`
example 2: `$img = 'http://www.smple.co.kr/~user/img';`

```perl
$adps = '0000';
```

관리자패스워드입니다. 반드시 변경해주세요.

The administrator password. Please change it.

```perl
$lockkey = 2;
```

lock key를 사용하는 경우 2나 1로 설정합니다. 락은 동시 접속으로 인한 데이터 손실을 방지하는 안전장치입니다. 2가 더 안정적이지만, 서버에 따라 사용할 수 없는 경우도 있으므로, 그런 경우에는 1로 설정해주세요.

If you use a lock key, set it to 2 or 1. The lock is a safety device to prevent data loss due to simultaneous access. 2 is more stable, but in some cases, it may not be available on the server, so set it to 1 in such cases.

※ 그 외의 변경·수정 사항은 스크립트 내에 설명되어 있으니 해당 내용을 참조해주세요.
※ For other changes and modifications, please refer to the description in the script.
