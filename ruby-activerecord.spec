#
# TODO
# - rip out vendor libraries: mysql.rb, sqlite.rb, simple.rb
#
Summary:	Object-Relational mapping library for Ruby
Summary(pl):	Biblioteka odwzorowañ obiektowo-relacyjnych dla Ruby
Name:		ruby-ActiveRecord
%define tarname activerecord
Version:	1.12.1
Release:	2
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/6569/%{tarname}-%{version}.tgz
# Source0-md5:	225d3df8fe7a554dfea1a75e91e2605d
Patch0:		%{name}-sanity.patch
URL:		http://activerecord.rubyonrails.org/
BuildRequires:	rpmbuild(macros) >= 1.263
BuildRequires:	ruby-modules
Requires:	ruby-modules
Requires:	ruby-ActiveSupport
Requires:	ruby-transaction-simple
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains Object-Relational mapping library for Ruby.

%description -l pl
Ten pakiet zawiera bibliotekê odwzorowañ obiektowo-relacyjnych dla
Ruby.

%prep
%setup -q -n %{tarname}-%{version}
%patch0 -p1
rm -r lib/active_record/vendor

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc README
%{ruby_rubylibdir}/*
%{ruby_ridir}/ActiveRecord
