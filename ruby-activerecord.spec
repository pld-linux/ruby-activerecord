%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
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

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{ruby_rubylibdir}
cp -a lib/* $RPM_BUILD_ROOT/%{ruby_rubylibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/*
