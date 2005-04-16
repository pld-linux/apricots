Summary:	Game where you fly a little plane around the screen and shoot things and drop bombs
Summary(pl):	Gra, polegaj±ca na lataniu samolotem, strzelaniu do ró¿nych rzeczy i zrzucaniu bomb
Name:		apricots
Version:	0.2.6
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.fishies.org.uk/%{name}-%{version}.tar.gz
# Source0-md5:	910828d717e46d8cbd9c24f702d09fbc
Patch0:		%{name}-destdir.patch
URL:		http://www.fishies.org.uk/apricots.html
BuildRequires:	OpenAL-devel
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Game where you fly a little plane around the screen and shoot things
and drop bombs.

%description -l pl
Gra, polegaj±ca na lataniu samolotem, strzelaniu do ró¿nych rzeczy
i zrzucaniu bomb.

%prep
%setup -q
%patch0 -p1

%build
cp /usr/share/automake/config.sub admin
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO apricots.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
