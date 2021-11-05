#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBE793007AD22DF7E (tsujan2000@gmail.com)
#
Name     : lxqt-runner
Version  : 0.17.0
Release  : 8
URL      : https://github.com/lxqt/lxqt-runner/releases/download/0.17.0/lxqt-runner-0.17.0.tar.xz
Source0  : https://github.com/lxqt/lxqt-runner/releases/download/0.17.0/lxqt-runner-0.17.0.tar.xz
Source1  : https://github.com/lxqt/lxqt-runner/releases/download/0.17.0/lxqt-runner-0.17.0.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: lxqt-runner-bin = %{version}-%{release}
Requires: lxqt-runner-data = %{version}-%{release}
Requires: lxqt-runner-license = %{version}-%{release}
Requires: lxqt-runner-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kwindowsystem-dev
BuildRequires : liblxqt-dev
BuildRequires : lxqt-build-tools
BuildRequires : lxqt-globalkeys-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(muparser)
BuildRequires : qtbase-dev
BuildRequires : qttools-dev

%description
# lxqt-runner
## Overview
lxqt-runner provides a GUI that comes up on the desktop and allows for launching applications or shutting down the system.

%package bin
Summary: bin components for the lxqt-runner package.
Group: Binaries
Requires: lxqt-runner-data = %{version}-%{release}
Requires: lxqt-runner-license = %{version}-%{release}

%description bin
bin components for the lxqt-runner package.


%package data
Summary: data components for the lxqt-runner package.
Group: Data

%description data
data components for the lxqt-runner package.


%package license
Summary: license components for the lxqt-runner package.
Group: Default

%description license
license components for the lxqt-runner package.


%package man
Summary: man components for the lxqt-runner package.
Group: Default

%description man
man components for the lxqt-runner package.


%prep
%setup -q -n lxqt-runner-0.17.0
cd %{_builddir}/lxqt-runner-0.17.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1636136213
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1636136213
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lxqt-runner
cp %{_builddir}/lxqt-runner-0.17.0/LICENSE %{buildroot}/usr/share/package-licenses/lxqt-runner/7fab4cd4eb7f499d60fe183607f046484acd6e2d
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lxqt-runner

%files data
%defattr(-,root,root,-)
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_ar.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_arn.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_ast.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_bg.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_ca.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_cs.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_cy.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_da.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_de.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_el.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_eo.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_es.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_es_VE.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_et.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_eu.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_fi.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_fr.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_gl.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_he.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_hr.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_hu.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_ia.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_id.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_it.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_ja.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_ko.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_lt.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_nb_NO.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_nl.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_pl.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_pt.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_pt_BR.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_ro_RO.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_ru.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_si.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_sk.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_sl.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_sr@latin.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_sr_BA.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_sr_RS.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_th_TH.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_tr.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_uk.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_zh_CN.qm
/usr/share/lxqt/translations/lxqt-runner/lxqt-runner_zh_TW.qm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lxqt-runner/7fab4cd4eb7f499d60fe183607f046484acd6e2d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lxqt-runner.1
