%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	IMC
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - create and parse Internet Mail Consortium-style files
Summary(pl):	%{_pearname} - tworzenie i parsowanie plik�w typu Internet Mail Consortium
Name:		php-pear-%{_pearname}
Version:	0.3
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	48b2b15969f5f5aecaf8e76eef03a6d1
URL:		http://pear.php.net/package/File_IMC/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
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

%description -l pl
Ta klasa pozwala programowo tworzy� pliki vCard i vCalendar oraz
pobiera� tekst.

WA�NE: struktura tablic zmieni�a si� nieco w stosunku do
Contact_Vcard_Parse. Now� struktur� mo�na obejrze� w przyk�adzie.
U�ycie wzorc�w tak�e r�ni si� od Contact_Vcard, co r�wnie� mo�na
zobaczy� w przyk�adach.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/{sample.*,*.php}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
