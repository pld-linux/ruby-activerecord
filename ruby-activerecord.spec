%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"])')
%define	ruby_version	%(ruby -r rbconfig -e 'print Config::CONFIG["ruby_version"]')
Summary:	Object-Relational mapping library for Ruby
Summary(pl):	Biblioteka odwzorowañ obiektowo-relacyjnych dla Ruby
Name:		ruby-ActiveRecord
%define tarname activerecord
Version:	0.9.4
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/download.php/1216/%{tarname}-%{version}.tgz
# Source0-md5:	7eca936e2b5eb049a0f276a58c2fda95
uRL:		http://activerecord.rubyonrails.org/
BuildRequires:	ruby
Requires:	ruby
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This pachage contains Object-Relational mapping library for Ruby.

%description -l pl
Ten pakiet zawiera bibliotekê odwzorowañ obiektowo-relacyjnych dla
Ruby.

%prep
%setup -q -n %{tarname}-%{version}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc README
%{ruby_rubylibdir}/*
%{ruby_ridir}/ActiveRecord
