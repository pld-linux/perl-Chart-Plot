#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Chart
%define	pnam	Plot
Summary:	Chart::Plot - plot two dimensional data in an image
Summary(pl):	Chart::Plot - gaficzne przedstawianie dwuwymiarowych dane
Name:		perl-Chart-Plot
Version:	0.11
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	22105348d7ff33603e37fb470c0ce003
BuildRequires:	perl-devel >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-GD
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I wrote Chart::Plot to create images of some simple graphs of two
dimensional data. The other graphing interface modules to GD.pm I saw
on CPAN either could not handle negative data, or could only chart
evenly spaced horizontal data. (If you have evenly spaced or nonmetric
horizontal data and you want a bar or pie chart, I have successfully
used the GIFgraph and Chart::* modules, available on CPAN.)

%description -l pl
Ten modu³ zosta³ napisany do tworzena obrazów zawieraj±cych wykresy
dwuwymiarowych danych. Inne znane autorowi interfejsy do GD.pm nie
potrafi³y obs³u¿yæ danych ujemnych, albo potrafi³y przedstawiaæ tylko
dane o równym rozk³adzie (do przedstawienia danych o równym rozk³adzie
lub poziomych niemetrycznych danych na wykresie s³upkowym lub ko³owym
wystarcza modu³ GIFgraph i modu³y Chart::* dostêpne w CPAN).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demo.cgi $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
