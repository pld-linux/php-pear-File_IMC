%include	/usr/lib/rpm/macros.php
%define         _class          File
%define         _subclass       IMC
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Create and parse Internet Mail Consortium-style files
Summary(pl):	%{_pearname} - Tworzenie i parsowanie plików typu Internet Mail Consortium
Name:		php-pear-%{_pearname}
Version:	0.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	48b2b15969f5f5aecaf8e76eef03a6d1
URL:		http://pear.php.net/package/File_IMC/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
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

This class has in PEAR status: %{_status}.

%description -l pl
Ta klasa pozwala programowo tworzyæ pliki vCard i vCalendar oraz
pobieraæ tekst.

WA¯NE: struktura tablic zmieni³a siê nieco w stosunku do
Contact_Vcard_Parse. Now± strukturê mo¿na obejrzeæ w przyk³adzie.
U¿ycie wzorców tak¿e ró¿ni siê od Contact_Vcard, co równie¿ mo¿na
zobaczyæ w przyk³adach.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/{Build,Parse}

install %{_pearname}-%{version}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_class}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_class}/%{_subclass}/Build/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Build
install %{_pearname}-%{version}/%{_class}/%{_subclass}/Parse/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Parse

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{sample.*,*.php}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
