Summary:	Python extension module for Kerberos 5
Name:		python-krbV
Version:	1.0.13
Release:	1
License:	LGPL v2
Group:		Development/Languages
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	6faf75cd993c3d19b8ef7b6e8a66972b
URL:		http://people.redhat.com/mikeb/python-krbV
BuildRequires:	/bin/awk
BuildRequires:	krb5-devel >= 1.2.2
BuildRequires:	python-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
python-krbV allows python programs to use Kerberos 5
authentication/security.

%prep
%setup -q

%build
%configure \
	LIBNAME=%{_lib}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING krbV-code-snippets.py
%{py_sitedir}/krbVmodule.so
