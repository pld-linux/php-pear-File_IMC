%define		_status		beta
%define		_pearname	File_IMC
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - create and parse Internet Mail Consortium-style files
Summary(pl.UTF-8):	%{_pearname} - tworzenie i parsowanie plików typu Internet Mail Consortium
Name:		php-pear-%{_pearname}
Version:	0.5.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	133bfd47aef06de8838dc645ad14b800
URL:		http://pear.php.net/package/File_IMC/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows you to programmatically create a vCard or vCalendar, and fetch
the text.

IMPORTANT: The array structure has changed slightly from
Contact_Vcard_Parse. See the example output for the new structure.
Also different from Contact_Vcard is the use of a factory pattern.
Again, see the examples.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa pozwala programowo tworzyć pliki vCard i vCalendar oraz
pobierać tekst.

WAŻNE: struktura tablic zmieniła się nieco w stosunku do
Contact_Vcard_Parse. Nową strukturę można obejrzeć w przykładzie.
Użycie wzorców także różni się od Contact_Vcard, co również można
zobaczyć w przykładach.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

install -d examples
mv docs/File_IMC/docs/sample.* examples
mv docs/File_IMC/docs/*example.php examples

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/File/*.php
%{php_pear_dir}/File/IMC

%{_examplesdir}/%{name}-%{version}
