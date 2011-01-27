%define		trac_ver	0.12
%define		plugin		sqlhelper
Summary:	Helper functions to make Trac SQL DB query more API-ish
Name:		trac-plugin-%{plugin}
Version:	0.2.1
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://trac-hacks.org/changeset/latest/tracsqlhelperscript?old_path=/&filename=%{plugin}-%{version}&format=zip#/%{plugin}-%{version}.zip
# Source0-md5:	7ab69c8b26d438465fa184f4c5afa710
URL:		http://trac-hacks.org/wiki/TracSqlHelperScript
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
Requires:	trac >= %{trac_ver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
While there is considerable contention on the subject, I am one of
those people that doesn't like to see SQL statements in python code
(or C code, etc). I especially don't like it when the same basic
statements are repeated all over the place. So TracSqlHelperScript is
my attempt to encapsulate all of this logic in one place. These are
functions I've already co-written for the TracHoursPlugin and then
rewritten (some of them) for the GeoTicketPlugin

%prep
%setup -qc
mv trac%{plugin}script/%{trac_ver}/* .

%build
%{__python} setup.py build
%{__python} setup.py egg_info

ver=$(awk '$1 == "Version:" {print $2}' *.egg-info/PKG-INFO)
test "$ver" = %{version}

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--single-version-externally-managed \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

# NOTE: no post registration needed, plugin not used directly

%files
%defattr(644,root,root,755)
%doc whitepaper.txt
%{py_sitescriptdir}/trac%{plugin}
%{py_sitescriptdir}/TracSQLHelper-*.egg-info
