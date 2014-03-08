#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Locale
%define		pnam	Msgfmt
%include	/usr/lib/rpm/macros.perl
Summary:	Locale::Msgfmt - Compile .po files to .mo files
Summary(pl.UTF-8):	Locale::Msgfmt - kompilacja plików .po do .mo
Name:		perl-Locale-Msgfmt
Version:	0.15
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Locale/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7e6fde43db034f765f3a425dfa1dd4d8
URL:		http://search.cpan.org/dist/Locale-Msgfmt/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-devel >= 1:5.8.5
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.80
BuildRequires:	perl-Test-Simple >= 0.47
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Locale::Msgfmt is a pure Perl reimplementation of msgfmt from GNU
gettext.

%description -l pl.UTF-8
Locale::Msgfmt to reimplementacja w czystym Perlu narzędzia msgfmt z
pakietu GNU gettext.

%package -n perl-Module-Install-Msgfmt
Summary:	Locale::Msgfmt support for Module::Install
Summary(pl.UTF-8):	Obsługa Locale::Msgfmt dla Module::Install
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	perl-Module-Install

%description -n perl-Module-Install-Msgfmt
Locale::Msgfmt rules support for Module::Install.

%description -n perl-Module-Install-Msgfmt -l pl.UTF-8
Obsługa reguł Locale::Msgfmt dla Module::Install.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Locale/Msgfmt.pm
%{perl_vendorlib}/Locale/Msgfmt
%{_mandir}/man3/Locale::Msgfmt*.3pm*

%files -n perl-Module-Install-Msgfmt
%defattr(644,root,root,755)
%{perl_vendorlib}/Module/Install/Msgfmt.pm
