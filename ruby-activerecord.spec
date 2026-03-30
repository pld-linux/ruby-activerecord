%define pkgname activerecord
Summary:	Object-Relational mapping library for Ruby
Summary(pl.UTF-8):	Biblioteka odwzorowań obiektowo-relacyjnych dla Ruby
Name:		ruby-%{pkgname}
Version:	8.1.2
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	85092d599f0ad89ba4991e7c46bebbf3
URL:		https://rubyonrails.org
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
Requires:	ruby-activemodel = %{version}
Requires:	ruby-activesupport = %{version}
Requires:	ruby-timeout >= 0.4.0
Provides:	ruby-ActiveRecord
Obsoletes:	ruby-ActiveRecord
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

rdoc --ri --op ri lib
rdoc --op rdoc lib
rm ri/created.rid
rm ri/cache.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{pkgname}-%{version}-%{release}

# install gemspec
install -d $RPM_BUILD_ROOT%{ruby_specdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.rdoc
%{ruby_vendorlibdir}/active_record
%{ruby_vendorlibdir}/active_record.rb
%{ruby_vendorlibdir}/arel
%{ruby_vendorlibdir}/arel.rb
%{ruby_vendorlibdir}/rails/generators/active_record.rb
%{ruby_vendorlibdir}/rails/generators/active_record
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{pkgname}-%{version}-%{release}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/ActiveRecord
%{ruby_ridir}/Arel
%{ruby_ridir}/lib/active_record/railties/page-databases_rake.ri
%{ruby_ridir}/lib/rails/generators/active_record
