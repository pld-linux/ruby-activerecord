#
# TODO
# - rip out vendor libraries: mysql.rb, sqlite.rb, simple.rb
#
%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"])')
%define	ruby_version	%(ruby -r rbconfig -e 'print Config::CONFIG["ruby_version"]')
Summary:	Object-Relational mapping library for Ruby
Summary(pl):	Biblioteka odwzorowañ obiektowo-relacyjnych dla Ruby
Name:		ruby-ActiveRecord
%define tarname activerecord
Version:	1.11.0
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/5111/%{tarname}-%{version}.tgz
# Source0-md5:	caaa795595cb012890a811167f184b3f
Patch0:		%{name}-sanity.patch
URL:		http://activerecord.rubyonrails.org/
BuildRequires:	ruby
Requires:	ruby
Requires:	ruby-ActiveSupport
Requires:	ruby-transaction-simple
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This pachage contains Object-Relational mapping library for Ruby.

%description -l pl
Ten pakiet zawiera bibliotekê odwzorowañ obiektowo-relacyjnych dla
Ruby.

%prep
%setup -q -n %{tarname}-%{version}
%patch0 -p1

%build
rm lib/active_record/vendor -r
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
