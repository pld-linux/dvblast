Summary:	DVB/ASI network streamer
Name:		dvblast
Version:	1.2
Release:	1
License:	GPL v2+
Group:		Networking
Source0:	http://downloads.videolan.org/pub/videolan/dvblast/1.2/%{name}-%{version}.tar.bz2
# Source0-md5:	009166092b1e99524b7599c218081a49
URL:		http://www.videolan.org/projects/dvblast.html
BuildRequires:	libdvbpsi-devel >= 0.1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple and powerful MPEG-2/TS demux and streaming application.
Features:
* Lightweight program designed for extreme memory and CPU conditions
* CAM menus (MMI) support via an external application
* The configuration file describing outputs can be reloaded without
  losing a single packet
* Support for the new S2API of linux-dvb
* IPv6 network support
* UDP rather than RTP output for IPTV STBs which don't support RTP
DVBlast is written to be the core of a custom IRD, CID, or ASI
gateway, based on a PC with a Linux-supported card. It is very
lightweight and stable, designed for 24/7 operation.
DVBlast does not do any kind of processing on the elementary streams,
such as transcoding, PID remapping or remultiplexing. If you were
looking for these features, switch to VLC. It does not stream from
plain files (have a look at multicat instead).
DVBlast supports several input methods:
* linux-dvb-supported cards (DVB-S, DVB-S2, DVB-C, DVB-T...) with or
  without CI interface,
* DVB-ASI cards,
* UDP or RTP stream carrying a transport stream.
It outputs one or several RTP streams carrying transport streams with:
* hardware or software PID filtering,
* PID-based or service-based demultiplexing,
* optional descrambling via CAM device,
* EIT, SDT and TDT pass-through for EPG information.

%prep
%setup -q

%build
export CFLAGS="%{rpmcflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}*
%{_mandir}/man1/%{name}.1*
