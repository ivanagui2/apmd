Summary:	Advanced Power Management (APM) utilities for notebooks
Summary(cs):	N�stroje pro APM (Advanced Power Management) BIOS na laptopech
Summary(da):	Avanceret str�mstyring (APM) bios v�rkt�jer for b�rbare
Summary(de):	Advanced Power Management (APM) BIOS-Dienstprogramme f�r Laptops
Summary(es):	Utilitarios para APM (Gesti�n Avanzado de Energ�a) BIOS para port�tiles
Summary(fr):	Utilitaires BIOS de gestion avanc�e de l'�nergie (APM) pour les ordinateurs portables
Summary(id):	Advanced Power Management (APM) BIOS utilities untuk laptop
Summary(is):	T�l sem stj�rnar orkunotkun fart�lvu (Advanced Power Management)
Summary(it):	Utility APM (Advanced Power Management) BIOS per laptop
Summary(ja):	��åץȥå��Ѥ� APM (Advanced Power Management) �桼�ƥ���ƥ�
Summary(no):	Advanced Power Management (APM) BIOS verkt�y for b�rbare
Summary(pl):	Obs�uga zarz�dzania enerig� (APM) dla notebook�w
Summary(pt):	Utilit�rios Advanced Power Management (APM) para port�teis
Summary(pt_BR):	Utilit�rios para APM (Gerenciamento Avancado de Energia)
Summary(ru):	������� ��� Advanced Power Management (APM) BIOS � ��������
Summary(sk):	Pom�cky pre Advanced Power Management (APM) BIOS laptopov
Summary(sl):	Pripomo�ki za prenosnike z Advanced Power Management (APM)
Summary(sv):	Verktyg f�r styrning av sp�nningshantering (APM) i b�rbara datorer
Summary(uk):	���̦�� ��� Advanced Power Management (APM) BIOS � ��������
Summary(zh_CN):	����ϥ���ͼ�����ĸ߼���Դ���� (APM) BIOS ʵ�ó���
Name:		apmd
Version:	3.0.2
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://www.worldvisions.ca/~apenwarr/apmd/%{name}-%{version}.tar.gz
Source1:	%{name}.init
Patch0:		%{name}-security.patch
Patch1:		%{name}-spinlock.patch
URL:		http://www.worldvisions.ca/~apenwarr/apmd/
BuildRequires:	XFree86-devel
Prereq:		/sbin/chkconfig
Obsoletes:	acpid
Requires:	procps
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86} ppc

%description
Advanced Power Management daemon and utilities allows you to watch
your notebook's power state and warn all users when the battery is
low. It can also handle some power state events automatically.

%description -l cs
APMD je sada program� pro ovl�d�n� d�mona pro pokro�ilou spr�vu
energie (Advanced Power Management - APM) v�etn� pomocn�ch program�,
kter� jsou k dispozici na v�t�in� modern�ch p�enosn�ch po��ta��. APMD
um� sledovat stav baterie notebooku a varovat u�ivatele p�i poklesu
jej�ho nap�t�. APMD je tak� schopn� vypnout PCMCIA sokety p�ed usp�n�m
po��ta�e.

%description -l da
APMD er et s�t programmer for kontrol af Advanced Power Management
(APM) d�monen og v�rkt�jer som findes i de fleste moderne b�rbare
datamaskiner. APMD kan overv�ge batteriet p� din b�rbare og advare dig
n�r batteriniveauet er lavt og/eller lukke ned for PCMCIA kortene f�r
maskinen g�r i dvale.

%description -l de
APMD enth�lt Programme zur Steuerung des Advanced Power Management
(APM)-Daemons und der Dienstprogramme, die in den meisten modernen
Laptops verwendet werden. APMD kann den Akku von Notebooks �berwachen
und Benutzer �ber eine zu geringe Ladung informieren. APMD kann
au�erdem die PCMCIA-Schnittstellen herunterfahren, bevor der Computer
in den Suspend-Modus schaltet.

%description -l es
Utilitarios y servidor para gesti�n avanzada de energ�a (APM).
Verifica la bater�a de tu notebook y avisa a los usuarios cuando la
carga es poca. Fue adicionado un patch no oficial para parar los
enchufes PCMCIA antes de una suspensi�n de energ�a.

%description -l fr
APMD est un ensemble de programmes permettant de contr�ler le d�mon
APM (Advanced Power Management) et les utilitaires install�s sur la
plupart des ordinateurs portables r�cents. APMD peut surveiller la
batterie de votre portable, vous avertir lorsqu'elle est faible ou
arr�ter les supports PCMCIA avant l'arr�t de votre ordinateur.

%description -l id
APMD adalah sekumpulan program yang melakukan kontrol terhadap
Advanced Power Management, deamon dan utility yang dapat ditemukan
hampir di semua laptop moderen. APMD dapat mengawasi penggunaan
baterai pada notebook, dan memberikan peringatan kepada pengguna bila
tenaga bateri rendah. APMD juga mampu melakukan shut down socket
PCMCIA sebelum suspend.

%description -l is
APMD er safn forrita til a� stj�rna APM ( Advanced Power Management -
st�ring rafnotkunar ) st�ringum sem er a� finna � flestum fart�lvum.
APMD getur fylgst me� �standi rafhl��unnar og l�ti� notendur vita
�egar rafmagn fer a� �rj�ta. APMD getur einnig sl�kkt � PCMCIA
�j�nustum ��ur en sl�kkt er � v�linni.

%description -l it
APDM � un set di programmi per il controllo del demone e delle utility
di Advanced Power Management (APM) presenti nella maggior parte dei
laptop moderni. APDM consente di controllare la batteria del portatile
e di avvisare gli utenti quando � quasi scarica e/o di chiudere gli
attacchi del PCMCIA prima di un'interruzione.

%description -l ja
APMD �ϺǶ�Υ�åץȥåץ���ԥ塼�����Ѥ����� Advanced Power
Management (APM) �ǡ����ȥ桼�ƥ���ƥ������椹�뤿��Υץ����
���åȤǤ��� APMD �ϥΡ��ȥ֥å��ΥХåƥ��ƻ뤷�����̤����ʤ�
�ʤ�ȷٹ𤷤��ꡢ�����ڥ�ɥ⡼�ɤ��ڤ��ؤ������ PCMCIA ��
����åȥ����󤷤��ꤷ�ޤ���

%description -l no
APMD er et sett programmer for kontroll av Advanced Power Management
(APM) daemonen og verkt�y som finnes i de fleste moderne b�rbare
datamaskiner. APMD kan overv�ke batteriet p� din b�rbare og advare deg
brukere n�r batteriniv�et er lavt og/eller stenge ned PCMCIA
kontaktene f�r maskinen g�r i dvale.

%description -l pl
Demon zadz�dzania energi� APM (Advanced Power Management) wraz z
programami pomocniczymi. Dzi�ki nim mo�liwe jest monitorowanie stanu
zasilania Twojego notebooka i ostrzeganie wszystkich u�ytkownik�w o
ko�cz�cej si� baterii, jak r�wnie� automatyczne reagowanie na zmiany.

%description -l pt
O APMD � um conjunto de programas e utilit�rios para controlar o APM
(Advanced Power Management ou Gest�o de Energia Avan�ada) existente na
maioria dos computadores port�teis modernos. O APMD pode vigiar a
bateria do seu port�til e avis�-lo quando a bateria est� em baixo e/ou
desligar os 'sockets' PCMCIA antes de suspender.

%description -l pt_BR
Utilit�rios e servidor para gerenciamento avan�ado de energia (APM).
Ele verifica a bateria de seu notebook e avisa aos usu�rios que ele
est� com pouca carga. Foi adicionado um patch nao oficial para parar
os soquetes PCMCIA antes de uma suspensao de energia.

%description -l ru
APMD - ��� ����� �������� ��� ���������� ������� APM (Advanced Power
Management) � ���������, ������������ �� ����������� �����������
����������� �����������. APMD ����� ������� �� ���������� �������
������������ ���������� � ������������� ������������ �� �� ��������.
����� ����, APMD ����� ��������� ������� PCMCIA ����� ��������� �
����� ����������� �����������������.

%description -l sk
APMD je sada programov pre riadenie syst�mu APM (Advanced Power
Management), nach�dzaj�ceho sa vo v��ine modern�ch prenosn�ch
po��ta�ov. APMD je schopn� kontrolova� bat�riu v�ho notebooku a
varova� pou��vate�ov, pokia� je skoro vybit�. M��e tie� odp�ja� PCMCIA
sokety pred \"uspan�m\"

%description -l sv
APMD �r program f�r att styra demon och verktyg f�r str�mhantering
(Advanced Power Management, APM) som finns i de flesta moderna b�rbara
datorer. APMD kan bevaka din b�rbaras batteri och varna dig n�r
batteriet sinar och/eller st�nga av PCMCIA-uttag f�re suspendering.

%description -l uk
APMD - �� ��¦� ������� ��� ��������� ������� Advanced Power
Management. APMD ���� �̦������� �� ��������� ������ ������� ��
������������� ���������ަ� ��� �����Ħ �������.

%description -l zh_CN
APMD
��һ��������ڿ�������ϥ���ͼ�����ϵĸ߼���Դ�����̨�����ʵ�ó���
APMD
���Լ�رʼǱ�������ĵ��״̬�������ڵ�ص�������ʱ���û��������档
APMD ���������ݹ�ǰ�ر� PCMCIA ��ۡ�

%package devel
Summary:	Header files and static library for developing APM applications
Summary(es):	Archivos de inclusi�n y bibliotecas para apmd en versi�n est�tica
Summary(pl):	Pliki nag��wkowe i biblioteka statyczna do tworzenia aplikacji korzystaj�cych z APM
Summary(pt_BR):	Arquivos de inclus�o e bibliotecas para o apmd em vers�o est�tica
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files necessary for developing APM applications.

%description devel -l es
Archivos de inclusi�n y bibliotecas para apmd en versi�n est�tica

%description devel -l pl
Pliki nag��wkowe niezb�dne do tworzenia aplikacji korzystaj�cych z
APM.

%description devel -l pt_BR
Arquivos de inclus�o e bibliotecas para o apmd em vers�o est�tica

%package -n xapm
Summary:	XFree86 APM monitoring and management tool
Summary(pl):	Narz�dzie do monitorowania i zarz�dzania APMem pod XFree86
Group:		X11/Applications
Requires:	XFree86

%description -n xapm
xapm is an XFree86 version of console APM client - "apm".

%description -n xapm -l pl
xapm jest wersj� konsolowego klienta APM - "apm", przenaczon� dla
XFree86.

%prep
%setup -q -n apmd
%patch0 -p1

%ifarch ppc
%patch1 -p1 
%endif 

%build
%{__make} CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" APMD_PROXY_DIR=%{_sbindir}
%{__make} -C xbattery clean
%{__make} CCOPTIONS="%{rpmcflags}" LOCAL_LDFLAGS="%{rpmldflags}" -C xbattery

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir},%{_sbindir}} \
	$RPM_BUILD_ROOT%{_prefix}/X11R6/{bin,man/man1} \
	$RPM_BUILD_ROOT{%{_mandir}/man{1,8},%{_sysconfdir}/{rc.d/init.d,sysconfig}}

install apm apmsleep on_ac_power $RPM_BUILD_ROOT%{_bindir}
install apmd apmd_proxy $RPM_BUILD_ROOT%{_sbindir}

install xapm $RPM_BUILD_ROOT%{_prefix}/X11R6/bin

install apm.1 apmsleep.1 $RPM_BUILD_ROOT%{_mandir}/man1/
install apmd.8 $RPM_BUILD_ROOT%{_mandir}/man8/
install xapm.1 $RPM_BUILD_ROOT%{_prefix}/X11R6/man/man1/xapm.1x
install xbattery/xbattery.man $RPM_BUILD_ROOT%{_prefix}/X11R6/man/man1/xbattery.1x

install libapm.a $RPM_BUILD_ROOT%{_libdir}
install apm.h $RPM_BUILD_ROOT%{_includedir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/apmd
install xbattery/xbattery $RPM_BUILD_ROOT%{_prefix}/X11R6/bin

cat << EOF > $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/apmd
APMD_OPTIONS="-p 10 -w 5 -W -P %{_sbindir}/apmd_proxy"
EOF

gzip -9nf README README.transfer ChangeLog ANNOUNCE

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add apmd
if [ -f /var/lock/subsys/apmd ]; then
	/etc/rc.d/init.d/apmd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/apmd start\" to start apmd daemon."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/apmd ]; then
		/etc/rc.d/init.d/apmd stop 1>&2
	fi
	/sbin/chkconfig --del apmd
fi

%files
%defattr(644,root,root,755)
%doc *.gz
%{_mandir}/man*/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(754,root,root) /etc/rc.d/init.d/apmd
%config(noreplace) /etc/sysconfig/apmd

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.a

%files -n xapm
%defattr(644,root,root,755)
%{_prefix}/X11R6/man/man*/*
%attr(755,root,root) %{_prefix}/X11R6/bin/*
