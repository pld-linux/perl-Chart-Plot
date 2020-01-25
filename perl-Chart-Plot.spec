#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Chart
%define		pnam	Plot
Summary:	Chart::Plot - plot two dimensional data in an image
Summary(pl.UTF-8):	Chart::Plot - gaficzne przedstawianie dwuwymiarowych dane
Name:		perl-Chart-Plot
Version:	0.11
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	22105348d7ff33603e37fb470c0ce003
URL:		http://search.cpan.org/dist/Chart-Plot/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-GD
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I wrote Chart::Plot to create images of some simple graphs of two
dimensional data. The other graphing interface modules to GD.pm I saw
on CPAN either could not handle negative data, or could only chart
evenly spaced horizontal data. (If you have evenly spaced or nonmetric
horizontal data and you want a bar or pie chart, I have successfully
used the GIFgraph and Chart::* modules, available on CPAN.)

%description -l pl.UTF-8
Ten moduł został napisany do tworzenia obrazów zawierających wykresy
dwuwymiarowych danych. Inne znane autorowi interfejsy do GD.pm nie
potrafiły obsłużyć danych ujemnych, albo potrafiły przedstawiać tylko
dane o równym rozkładzie (do przedstawienia danych o równym rozkładzie
lub poziomych niemetrycznych danych na wykresie słupkowym lub kołowym
wystarcza moduł GIFgraph i moduły Chart::* dostępne w CPAN).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demo.cgi $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
