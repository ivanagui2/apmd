Summary:	Advanced Power Management (APM) utilities for notebooks
Summary(pl):	Obs�uga zarz�dzania enerig� (APM) dla notebook�w
Summary(pt_BR):	Utilit�rios para APM (Gerenciamento Avancado de Energia)
Summary(es):	Utilitarios para APM (Gesti�n Avanzado de Energ�a)
Name:		apmd
Version:	3.0.2
Release:	2
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://www.worldvisions.ca/~apenwarr/apmd/%{name}-%{version}.tar.gz
Source1:	%{name}.init
Patch0:		%{name}-security.patch
URL:		http://www.worldvisions.ca/~apenwarr/apmd/
Requires:	procps
Prereq:		/sbin/chkconfig
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}

%description
Advanced Power Management daemon and utilities allows you to watch
your notebook's power state and warn all users when the battery is
low. It can also handle some power state events automatically.

%description -l pl
Demon zadz�dzania energi� APM (Advanced Power Management) wraz z
programami pomocniczymi. Dzi�ki nim mo�liwe jest monitorowanie stanu
zasilania Twojego notebooka i ostrzeganie wszystkich u�ytkownik�w o
ko�cz�cej si� baterii, jak r�wnie� automatyczne reagowanie na zmiany.

%description -l pt_BR
Utilit�rios e servidor para gerenciamento avan�ado de energia (APM). Ele
verifica a bateria de seu notebook e avisa aos usu�rios que ele est� com pouca
carga.

Foi adicionado um patch nao oficial para parar os soquetes PCMCIA antes de uma
suspensao de energia.

%description -l es
Utilitarios y servidor para gesti�n avanzada de energ�a (APM). Verifica la
bater�a de tu notebook y avisa a los usuarios cuando la carga es poca.  Fue
adicionado un patch no oficial para parar los enchufes PCMCIA antes de una
suspensi�n de energ�a.

%package devel
Summary:	Header files for developing APM applications
Summary(pl):	Pliki nag��wkowe do tworzenia aplikacji korzystaj�cych z APM
Summary(pt_BR):	Arquivos de inclus�o e bibliotecas para o apmd em vers�o est�tica
Summary(es):	Archivos de inclusi�n y bibliotecas para apmd en versi�n est�tica
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files necessary for developing APM applications.

%description devel -l pl
Pliki nag��wkowe niezb�dne do tworzenia aplikacji korzystaj�cych z
APM.

%description -l pt_BR devel
Arquivos de inclus�o e bibliotecas para o apmd em vers�o est�tica

%description -l es devel
Archivos de inclusi�n y bibliotecas para apmd en versi�n est�tica

%package -n xapm
Summary:	XFree86 APM monitoring and management tool
Summary(pl):	Narz�dzie do monitorowania i zarz�dzania APMem pod XFree86
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	XFree86

%description -n xapm
xapm is an XFree86 version of console APM client - "apm".

%description -n xapm -l pl
xapm jest wersj� konsolowego klienta APM - "apm", przenaczon� dla
XFree86.

%prep
%setup -q -n apmd
%patch0 -p1

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
