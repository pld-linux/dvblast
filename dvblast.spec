# TODO: libstreammaster (Deltacast ASI cards SDK) support
Summary:	DVB/ASI network streamer
Summary(pl.UTF-8):	Aplikacja do tworzenia strumieni sieciowych DVB/ASI
Name:		dvblast
Version:	3.1
Release:	1
License:	GPL v2+
Group:		Networking
Source0:	http://downloads.videolan.org/dvblast/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	f195fc6c64796d989bf29a3e2ffca758
URL:		http://www.videolan.org/projects/dvblast.html
BuildRequires:	bitstream
BuildRequires:	libev-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DVBlast is a simple and powerful MPEG-2/TS demux and streaming
application with several input methods:
 - Linux-supported DVB cards (DVB-S, DVB-S2, DVB-C, DVB-T...)
 - DVB-ASI cards
 - UDP or RTP stream carrying a transport stream

It outputs one or several RTP streams carrying transport streams with:
 - hardware or software PID filtering
 - PID-based or service-based demultiplexing
 - optional descrambling via CAM device
 - optional DVB tables

%description -l pl.UTF-8
DVBlast to prosta, ale mająca duże możliwości aplikacja
demultipleksująca MPEG-2/TS oraz generująca strumienie, mająca kilka
metod wejściowych:
 - karty DVB obsługiwane przez Linuksa (DVB-S, DVB-S3, DVB-C,
   DVB-T...)
 - karty DVB-ASI
 - strumienie UDP lub RTP niosące strumień transportowy

Wyjściem może być jeden lub kilka strumieni RTP niosących strumienie
transportowe z:
 - sprzętowym lub programowym filtrowaniem PID-ów
 - demultipleksowaniem w oparciu o PID-y lub usługi
 - opcjonalnym rozszyfrowywaniem poprzez urządzenie CAM
 - opcjonalnymi tablicami DVB

%prep
%setup -q

%build
export CFLAGS="%{rpmcflags}"
%{__make} \
	CC="%{__cc}" \
	V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/dvblast
%attr(755,root,root) %{_bindir}/dvblastctl
%attr(755,root,root) %{_bindir}/dvblast_mmi.sh
%{_mandir}/man1/dvblast.1*
