# TODO
# - rip out vendor libraries: mysql.rb, sqlite.rb, simple.rb
#
%define pkgname activerecord
Summary:	Object-Relational mapping library for Ruby
Summary(pl.UTF-8):	Biblioteka odwzorowań obiektowo-relacyjnych dla Ruby
Name:		ruby-%{pkgname}
Version:	2.3.5
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	48a9ab7fbac97478fac9722fb5e14cda
Patch0:		%{name}-rubygems.patch
URL:		http://rubyforge.org/projects/activerecord/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-activesupport >= 2.0.1
Requires:	ruby-transaction-simple
Obsoletes:	ruby-ActiveRecord
Provides:	ruby-ActiveRecord
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
This package contains Object-Relational mapping library for Ruby.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę odwzorowań obiektowo-relacyjnych dla
Ruby.

%package rdoc
Summary:	Documentation files for ActiveRecord
Summary(pl.UTF-8):	Dokumentacja do biblioteki ActiveRecord
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for ActiveRecord.

%description rdoc -l pl.UTF-8
Dokumentacja do biblioteki ActiveRecord.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README  -o -print | xargs touch --reference %{SOURCE0}
%patch0 -p1

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{pkgname}-%{version}-%{release}

rm -f $RPM_BUILD_ROOT%{ruby_ridir}/created.rid
rm -rf $RPM_BUILD_ROOT%{ruby_ridir}/Fixture
rm -rf $RPM_BUILD_ROOT%{ruby_ridir}/FixtureClassNotFound
rm -rf $RPM_BUILD_ROOT%{ruby_ridir}/Fixtures
rm -rf $RPM_BUILD_ROOT%{ruby_ridir}/MysqlCompat
rm -rf $RPM_BUILD_ROOT%{ruby_ridir}/Test
rm -rf $RPM_BUILD_ROOT%{ruby_ridir}/YAML

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{ruby_rubylibdir}/active_record
%{ruby_rubylibdir}/active_record.rb
%{ruby_rubylibdir}/activerecord.rb

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{pkgname}-%{version}-%{release}
%{ruby_ridir}/ActiveRecord
