%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"])')
%define	ruby_version	%(ruby -r rbconfig -e 'print Config::CONFIG["ruby_version"]')
Summary:	Object-Relational mapping library for Ruby
Name:		ruby-ActiveRecord
%define tarname active_record
Version:	0.5
Release:	0
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubyforge.org/download.php/358/%{tarname}-%{version}.tgz
# Source0-md5:	49768acdfed8b28f3c75fa5fec6e3f33
URL:		http://activerecord.rubyforge.org/
BuildRequires:	ruby
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Object-Relational mapping library for Ruby

%prep
%setup -q -n %{tarname}-%{version}

%build
rm lib/%{tarname}/fixtures.rb
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{%{ruby_rubylibdir},%{ruby_ridir}}
cp -a lib/* $RPM_BUILD_ROOT/%{ruby_rubylibdir}
cp -a ri/ri/* $RPM_BUILD_ROOT/%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%{ruby_rubylibdir}/*
%{_datadir}/ri/%{ruby_version}/ActiveRecord
