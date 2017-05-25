#
# Conditional build:
%bcond_without	cdaudio		# don't build cdaudio plugin
%bcond_without	dirac		# don't build Dirac plugin
%bcond_without	directfb	# don't build directfb videosink plugin
%bcond_without	dts		# don't build DTS plugin
%bcond_without	faad		# don't build faad plugin
%bcond_without	gsm		# don't build gsm plugin
%bcond_without	ladspa		# don't build ladspa plugin
%bcond_without	mjpegtools	# don't build mpeg2enc plugin
%bcond_without	mms		# don't build mms plugin
%bcond_without	musepack	# don't build musepack plugin
%bcond_without	neon		# don't build neonhttpsrc plugin
%bcond_without	ofa		# don't build OFA plugin
%bcond_with	opencv		# don't build OpenCV plugin
%bcond_without	sdl		# don't build sdl plugin
%bcond_with	swfdec		# swfdec plugin
%bcond_without	spc		# don't build spc plugin
%bcond_without	wavpack		# don't build wavpack plugin
%bcond_without	xvid		# don't build XviD plugin
%bcond_without	amr		# don't build amrwbenc plugin
%bcond_with	divx4linux	# build divx4linux plugins
%bcond_without	vdpau		# build without VDPAU

%define		gstname		gst-plugins-bad
%define		gst_major_ver	0.10
%define		gst_req_ver	0.10.36
%define		gstpb_req_ver	0.10.36
%define		__gst_inspect	/usr/bin/gst-inspect-0.10
Summary:	Bad GStreamer Streaming-media framework plugins
Summary(pl.UTF-8):	Złe wtyczki do środowiska obróbki strumieni GStreamer
Name:		gstreamer0.10-plugins-bad
Version:	0.10.23
Release:	24
License:	LGPL v2+
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-bad/%{gstname}-%{version}.tar.bz2
# Source0-md5:	fcb09798114461955260e4d940db5987
Patch0:		gstreamer-plugins-bad-libdts.patch
Patch1:		gstreamer-plugins-bad-divx4linux.patch
Patch2:		gstreamer-plugins-bad-timidity.patch
Patch3:		gstreamer-plugins-bad-nas.patch
Patch4:		glib2_32.patch
Patch5:		docs-voamrwbenc.patch
Patch6:		gstreamer-plugins-bad-directfb.patch
Patch7:		gstreamer-plugins-bad-opencv.patch
Patch8:		gst-neon.patch
Patch9:		gstreamer-plugins-bad-modplug.patch
Patch10:	libvpx2.patch
Patch11:	gtk-doc.patch
URL:		http://gstreamer.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.10
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.17
# 2.22 for all, gio-2.26 for gsettings
BuildRequires:	glib2-devel >= 1:2.26
BuildRequires:	gstreamer0.10-devel >= %{gst_req_ver}
BuildRequires:	gstreamer0.10-plugins-base-devel >= %{gstpb_req_ver}
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	libtool >= 1.4
BuildRequires:	orc-devel >= 0.4.11
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	python >= 2.1
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	xorg-lib-libX11-devel
##
## plugins
##
%{?with_directfb:BuildRequires:	DirectFB-devel >= 1:0.9.24}
BuildRequires:	OpenAL-devel >= 1.13.0
%{?with_sdl:BuildRequires:	SDL-devel}
BuildRequires:	alsa-lib-devel >= 0.9.1
BuildRequires:	bzip2-devel
BuildRequires:	cairo-devel
BuildRequires:	celt-devel >= 0.11.0
BuildRequires:	curl-devel >= 7.21.0
%{?with_dirac:BuildRequires:	dirac-devel >= 0.10}
%{?with_divx4linux:BuildRequires:	divx4linux-devel >= 1:5.05.20030428}
BuildRequires:	exempi-devel >= 1.99.5
BuildRequires:	faac-devel
%{?with_faad:BuildRequires:	faad2-devel >= 2.0-2}
BuildRequires:	flite-devel
BuildRequires:	game-music-emu-devel >= 0.5.5
# when becomes available...
#BuildRequires:	game-music-emu-devel >= 0.5.6
BuildRequires:	gmyth-devel >= 0.7
BuildRequires:	jasper-devel
%{?with_ladspa:BuildRequires:	ladspa-devel >= 1.12}
BuildRequires:	libass-devel >= 0.9.4
%{?with_cdaudio:BuildRequires:	libcdaudio-devel}
BuildRequires:	libdc1394-devel >= 2.0.0
%{?with_dts:BuildRequires:	libdts-devel}
BuildRequires:	libdvdnav-devel >= 4.1.2
BuildRequires:	libdvdread-devel >= 4.1.2
BuildRequires:	libexif-devel >= 0.6.16
%{?with_gsm:BuildRequires:	libgsm-devel}
BuildRequires:	libiptcdata-devel >= 1.0.2
BuildRequires:	libkate-devel >= 0.1.7
BuildRequires:	liblrdf-devel
BuildRequires:	libmimic-devel >= 1.0
%{?with_mms:BuildRequires:	libmms-devel >= 0.4}
BuildRequires:	libmodplug-devel
%{?with_musepack:BuildRequires:	libmpcdec-devel >= 1.2}
BuildRequires:	libmusicbrainz-devel >= 2.1.0
%{?with_ofa:BuildRequires:	libofa-devel >= 0.9.3}
%{?with_spc:BuildRequires:	libopenspc-devel >= 0.3.99}
BuildRequires:	libpng-devel >= 2:1.2.0
BuildRequires:	librsvg-devel >= 2.14
BuildRequires:	librtmp-devel
BuildRequires:	libsndfile-devel >= 1.0.16
# for decklink, modplug, soundtouch
BuildRequires:	libstdc++-devel
BuildRequires:	libtheora-devel >= 1.0
BuildRequires:	libtiger-devel >= 0.3.2
BuildRequires:	libtimidity-devel
BuildRequires:	libvpx-devel
BuildRequires:	libx264-devel >= 0.1.2
%{?with_mjpegtools:BuildRequires:	mjpegtools-devel >= 2.0.0}
BuildRequires:	nas-devel
%{?with_neon:BuildRequires:	neon-devel >= 0.27.0}
%if %{with opencv}
BuildRequires:	opencv-devel < 1:2.5.0
BuildRequires:	opencv-devel >= 1:2.2.0
%endif
BuildRequires:	openssl-devel >= 0.9.5
BuildRequires:	opus-devel >= 0.9.4
BuildRequires:	schroedinger-devel >= 1.0.7
BuildRequires:	slv2-devel >= 0.6.6
BuildRequires:	soundtouch-devel >= 1.4
BuildRequires:	spandsp-devel >= 1:0.0.6
%if %{with swfdec}
BuildRequires:	swfdec-devel < 0.4.0
BuildRequires:	swfdec-devel >= 0.3.6
%endif
%{?with_vdpau:BuildRequires:	libvdpau-devel}
BuildRequires:	twolame-devel
BuildRequires:	vo-aacenc-devel >= 0.1.0
%{?with_amr:BuildRequires:	vo-amrwbenc-devel >= 0.1.0}
BuildRequires:	wildmidi-devel
BuildRequires:	xorg-lib-libX11-devel
%{?with_xvid:BuildRequires:	xvid-devel >= 1.3.0}
BuildRequires:	zbar-devel >= 0.9
BuildRequires:	zvbi-devel >= 0.2
Requires:	glib2 >= 1:2.26
Requires:	gstreamer0.10 >= %{gst_req_ver}
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Requires:	orc >= 0.4.11
Obsoletes:	gstreamer-quicktime
Obsoletes:	gstreamer-vcd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gstlibdir 	%{_libdir}/gstreamer-%{gst_major_ver}
%define		gstdatadir 	%{_datadir}/gstreamer-%{gst_major_ver}

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plugins.

%description -l pl.UTF-8
GStreamer to środowisko obróbki danych strumieniowych, bazujące na
grafie filtrów operujących na danych medialnych. Aplikacje używające
tej biblioteki mogą robić wszystko od przetwarzania dźwięku w czasie
rzeczywistym, do odtwarzania filmów i czegokolwiek innego związego z
mediami. Architektura bazująca na wtyczkach pozwala na łatwe dodawanie
nowych typów danych lub możliwości obróbki.

%package devel
Summary:	Header files and API documentation for gstapp library
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja API biblioteki gstapp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and API documentation for gstapp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja API biblioteki gstapp.

## Plugins ##

%package -n gstreamer0.10-aac
Summary:	GStreamer plugin for AAC audio encoding and decoding
Summary(pl.UTF-8):	Wtyczka do GStreamera do kodowania i dekodowania plików audio AAC
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Obsoletes:	gstreamer-aac < 1.0

%description -n gstreamer0.10-aac
GStreamer plugin for AAC audio encoding and decoding.

%description -n gstreamer0.10-aac -l pl.UTF-8
Wtyczka do GStreamera do kodowania i dekodowania plików audio AAC.

%package -n gstreamer0.10-amrwbenc
Summary:	GStreamer plugin for AMR-WB audio encoding
Summary(pl.UTF-8):	Wtyczka GStreamera do kodowania dźwięku w formacie AMR-WB
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Requires:	vo-amrwbenc >= 0.1.0
Obsoletes:	gstreamer-amrwbenc < 1.0

%description -n gstreamer0.10-amrwbenc
GStreamer plugin for AMR-WB audio encoding, using VisualOn library.

%description -n gstreamer0.10-amrwbenc -l pl.UTF-8
Wtyczka GStreamera do kodowania dźwięku w formacie AMR-WB,
wykorzystująca bibliotekę VisualOn.

%package -n gstreamer0.10-ass
Summary:	GStreamer plugin for ASS/SSA subtitles rendering
Summary(pl.UTF-8):	Wtyczka do GStreamera do renderowania napisów ASS/SSA
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Requires:	libass >= 0.9.4
Obsoletes:	gstreamer-ass < 1.0

%description -n gstreamer0.10-ass
GStreamer plugin for ASS/SSA subtitles rendering.

%description -n gstreamer0.10-ass -l pl.UTF-8
Wtyczka do GStreamera do renderowania napisów ASS/SSA.

%package -n gstreamer0.10-audio-effects-bad
Summary:	Bad GStreamer audio effects plugins
Summary(pl.UTF-8):	Złe wtyczki efektów dźwiękowych do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-audio-effects
Obsoletes:	gstreamer-audio-effects-bad < 1.0

%description -n gstreamer0.10-audio-effects-bad
Bad GStreamer audio effects plugins.

%description -n gstreamer0.10-audio-effects-bad -l pl.UTF-8
Złe wtyczki efektów dźwiękowych do GStreamera.

%package -n gstreamer0.10-audiosink-nas
Summary:	GStreamer NAS audio output plugin
Summary(pl.UTF-8):	Wtyczka wyjścia dźwięku NAS dla GStreamera
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Provides:	gstreamer0.10-audiosink = %{version}
Obsoletes:	gstreamer-audiosink-nas < 1.0
Obsoletes:	gstreamer-nas

%description -n gstreamer0.10-audiosink-nas
GStreamer NAS audio output plugin.

%description -n gstreamer0.10-audiosink-nas -l pl.UTF-8
Wtyczka wyjścia dźwięku NAS dla GStreamera.

%package -n gstreamer0.10-cdaudio
Summary:	GStreamer plugin for CD audio input using libcdaudio
Summary(pl.UTF-8):	Wtyczka do GStreamera odtwarzająca płyty CD-Audio przy użyciu libcdaudio
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-cdaudio < 1.0

%description -n gstreamer0.10-cdaudio
Plugin for playing audio tracks using libcdaudio under GStreamer.

%description -n gstreamer0.10-cdaudio -l pl.UTF-8
Wtyczka do odtwarzania ścieżek dźwiękowych pod GStreamerem za pomocą
libcdaudio.

%package -n gstreamer0.10-celt
Summary:	GStreamer Celt audio codec plugin
Summary(pl.UTF-8):	Wtyczka kodeka dźwięku Celt do GStreamera
Group:		Libraries
Requires:	celt >= 0.11.0
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-celt < 1.0

%description -n gstreamer0.10-celt
GStreamer Celt audio encoder and decoder plugin.

%description -n gstreamer0.10-celt -l pl.UTF-8
Wtyczka GStreamera kodująca i dekodująca dźwięk w formacie Celt.

%package -n gstreamer0.10-curl
Summary:	GStreamer cURL network sink plugin
Summary(pl.UTF-8):	Wtyczka wyjścia sieciowego cURL dla GStreamera
Group:		Libraries
Requires:	curl-libs >= 7.21.0
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-curl < 1.0

%description -n gstreamer0.10-curl
GStreamer network sink plugin that uses libcurl as a client to upload
data to a server (e.g. HTTP or FTP).

%description -n gstreamer0.10-curl -l pl.UTF-8
Wtyczka wyjścia sieciowego GStreamera wykorzystująca libcurl jako
klienta do wysyłania danych na serwer (np. HTTP lub FTP).

%package -n gstreamer0.10-dc1394
Summary:	GStreamer 1394 IIDC (Firewire digital cameras) video source plugin
Summary(pl.UTF-8):	Wtyczka źródła obrazu 1394 IIDC (z kamer cyfrowych Firewire) do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-dc1394 < 1.0

%description -n gstreamer0.10-dc1394
GStreamer 1394 IIDC (Firewire digital cameras) video source plugin.

%description -n gstreamer0.10-dc1394 -l pl.UTF-8
Wtyczka źródła obrazu 1394 IIDC (z kamer cyfrowych Firewire) do
GStreamera.

%package -n gstreamer0.10-dirac
Summary:	GStreamer Dirac plugin
Summary(pl.UTF-8):	Wtyczka Dirac do GStreamera
Group:		Libraries
Requires:	dirac >= 0.10
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-dirac < 1.0

%description -n gstreamer0.10-dirac
GStreamer Dirac video decoder/encoder plugin.

%description -n gstreamer0.10-dirac -l pl.UTF-8
Wtyczka dekodująca i kodująca obraz Dirac do GStreamera.

%package -n gstreamer0.10-divx
Summary:	GStreamer divx plugin
Summary(pl.UTF-8):	Wtyczka divx do GStreamera
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Obsoletes:	gstreamer-divx < 1.0

%description -n gstreamer0.10-divx
GStreamer divx plugin.

%description -n gstreamer0.10-divx -l pl.UTF-8
Wtyczka divx do GStreamera.

%package -n gstreamer0.10-dts
Summary:	GStreamer DTS plugin
Summary(pl.UTF-8):	Wtyczka DTS do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Obsoletes:	gstreamer-dts < 1.0

%description -n gstreamer0.10-dts
Plugin for DTS Coherent Acoustics support.

%description -n gstreamer0.10-dts -l pl.UTF-8
Wtyczka do GStreamera obsługująca DTS Coherent Acoustics.

%package -n gstreamer0.10-flite
Summary:	GStreamer Flite plugin
Summary(pl.UTF-8):	Wtyczka Flite do GStreamera
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Obsoletes:	gstreamer-flite < 1.0

%description -n gstreamer0.10-flite
Plugin for Flite support.

%description -n gstreamer0.10-flite -l pl.UTF-8
Wtyczka do GStreamera obsługująca Flite.

%package -n gstreamer0.10-gme
Summary:	GStreamer GME Audio Decoder plugin
Summary(pl.UTF-8):	Wtyczka dekodująca GME do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-gme < 1.0

%description -n gstreamer0.10-gme
GStreamer GME Audio Decoder plugin.

%description -n gstreamer0.10-gme -l pl.UTF-8
Wtyczka dekodująca GME do GStreamera.

%package -n gstreamer0.10-gsettings
Summary:	GStreamer GSettings plugin
Summary(pl.UTF-8):	Wtyczka GSettings do GStreamera
Group:		Libraries
Requires:	glib2 >= 1:2.26
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-gsettings < 1.0

%description -n gstreamer0.10-gsettings
GStreamer GSettings plugin.

%description -n gstreamer0.10-gsettings -l pl.UTF-8
Wtyczka GSettings do GStreamera.

%package -n gstreamer0.10-gsm
Summary:	GStreamer plugin for GSM lossy audio format
Summary(pl.UTF-8):	Wtyczka do GStreamera obsługująca stratny format dźwięku GSM
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Obsoletes:	gstreamer-gsm < 1.0

%description -n gstreamer0.10-gsm
Output plugin for GStreamer to convert to GSM lossy audio format.

%description -n gstreamer0.10-gsm -l pl.UTF-8
Wtyczka wyjścia dźwięku GSteamera konwertująca do stratnego formatu
GSM.

%package -n gstreamer0.10-kate
Summary:	GStreamer plugin for Kate text streams
Summary(pl.UTF-8):	Wtyczka obsługująca strumienie tekstowe Kate dla GStreamera
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Requires:	libkate >= 0.1.7
Requires:	libtiger >= 0.3.2
Obsoletes:	gstreamer-kate < 1.0

%description -n gstreamer0.10-kate
GStreamer plugin for Kate text streams.

%description -n gstreamer0.10-kate -l pl.UTF-8
Wtyczka obsługująca strumienie tekstowe Kate dla GStreamera.

%package -n gstreamer0.10-ladspa
Summary:	GStreamer wrapper for LADSPA plugins
Summary(pl.UTF-8):	Wrapper do wtyczek LADSPA dla GStreamera
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Obsoletes:	gstreamer-ladspa < 1.0

%description -n gstreamer0.10-ladspa
Plugin which wraps LADSPA plugins for use by GStreamer applications.

%description -n gstreamer0.10-ladspa -l pl.UTF-8
Wtyczka pozwalająca na używanie wtyczek LADSPA przez aplikacje
GStreamera.

%package -n gstreamer0.10-lv2
Summary:	GStreamer wrapper for LV2 plugins
Summary(pl.UTF-8):	Wrapper do wtyczek LV2 dla GStreamera
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Requires:	slv2 >= 0.6.6
Obsoletes:	gstreamer-lv2 < 1.0

%description -n gstreamer0.10-lv2
Plugin which wraps LV2 plugins for use by GStreamer applications.

%description -n gstreamer0.10-lv2 -l pl.UTF-8
Wtyczka pozwalająca na używanie wtyczek LV2 przez aplikacje
GStreamera.

%package -n gstreamer0.10-mimic
Summary:	GStreamer Mimic video decoding/encoding plugin
Summary(pl.UTF-8):	Wtyczka kodująca/dekodująca obraz Mimic do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-mimic < 1.0

%description -n gstreamer0.10-mimic
GStreamer Mimic video decoding/encoding plugin.

%description -n gstreamer0.10-mimic -l pl.UTF-8
Wtyczka kodująca/dekodująca obraz Mimic do GStreamera.

%package -n gstreamer0.10-mjpegtools
Summary:	GStreamer mpeg2enc plugin
Summary(pl.UTF-8):	Wtyczka mpeg2enc do GStreamera
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Requires:	mjpegtools-libs >= 2.0.0
Obsoletes:	gstreamer-mjpegtools < 1.0

%description -n gstreamer0.10-mjpegtools
GStreamer mpeg2enc plugin (based on mjpegtools libraries).

%description -n gstreamer0.10-mjpegtools -l pl.UTF-8
Wtyczka mpeg2enc do GStreamera (oparta na bibliotekach mjpegtools).

%package -n gstreamer0.10-mms
Summary:	GStreamer mms plugin
Summary(pl.UTF-8):	Wtyczka mms do GStreamera
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Requires:	libmms >= 0.4
Obsoletes:	gstreamer-mms < 1.0

%description -n gstreamer0.10-mms
GStreamer mms plugin.

%description -n gstreamer0.10-mms -l pl.UTF-8
Wtyczka mms do GStreamera.

%package -n gstreamer0.10-musepack
Summary:	GStreamer musepack plugin
Summary(pl.UTF-8):	Wtyczka musepack do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-musepack < 1.0

%description -n gstreamer0.10-musepack
GStreamer musepack plugin.

%description -n gstreamer0.10-musepack -l pl.UTF-8
Wtyczka musepack do GStreamera.

%package -n gstreamer0.10-mythtv
Summary:	GStreamer MythTV plugin
Summary(pl.UTF-8):	Wtyczka MythTV do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-mythtv < 1.0

%description -n gstreamer0.10-mythtv
GStreamer MythTV plugin.

%description -n gstreamer0.10-mythtv -l pl.UTF-8
Wtyczka MythTV do GStreamera.

%package -n gstreamer0.10-musicbrainz
Summary:	GStreamer musicbrainz plugin
Summary(pl.UTF-8):	Wtyczka musicbrainz do GStreamera
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Obsoletes:	gstreamer-musicbrainz < 1.0

%description -n gstreamer0.10-musicbrainz
GStreamer musicbrainz plugin - a TRM signature producer.

%description -n gstreamer0.10-musicbrainz -l pl.UTF-8
Wtyczka musicbrainz do GStreamera, tworząca sygnatury TRM.

%package -n gstreamer0.10-neon
Summary:	GStreamer neon HTTP source plugin
Summary(pl.UTF-8):	Wtyczka źródła HTTP neon do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Requires:	neon >= 0.27.0
Obsoletes:	gstreamer-neon < 1.0

%description -n gstreamer0.10-neon
GStreamer neon HTTP source plugin.

%description -n gstreamer0.10-neon -l pl.UTF-8
Wtyczka źródła HTTP neon do GStreamera.

%package -n gstreamer0.10-ofa
Summary:	GStreamer OFA fingerprint plugin
Summary(pl.UTF-8):	Wtyczka odcisków OFA do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Requires:	libofa >= 0.9.3
Obsoletes:	gstreamer-ofa < 1.0

%description -n gstreamer0.10-ofa
GStreamer OFA plugin to calculate MusicIP fingerprints from audio
files.

%description -n gstreamer0.10-ofa -l pl.UTF-8
Wtyczka OFA do GStreamera służąca do obliczania odcisków MusicIP
plików dźwiękowych.

%package -n gstreamer0.10-openal
Summary:	GStreamer OpenAL audio input/output plugin
Summary(pl.UTF-8):	Wtyczka wejścia/wyjścia dźwięku OpenAL do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Provides:	gstreamer0.10-audiosink = %{version}
Obsoletes:	gstreamer-openal < 1.0

%description -n gstreamer0.10-openal
GStreamer OpenAL support plugin, providing audio sink and source.

%description -n gstreamer0.10-openal -l pl.UTF-8
Wtyczka obsługująca OpenAL do GStreamera, zapewniająca wyjście i
źródło dźwięku.

%package -n gstreamer0.10-opencv
Summary:	GStreamer OpenCV plugin
Summary(pl.UTF-8):	Wtyczka OpenCV do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Requires:	opencv >= 1:2.2.0
Obsoletes:	gstreamer-opencv < 1.0

%description -n gstreamer0.10-opencv
GStreamer OpenCV plugin. It contains the following elements:
facedetect, faceblur, edgedetect, cvsobel, cvsmooth, cvlaplace,
cverode, cvequalizehist, cvdilate, textwrite, templatematch,
pyramidsegment.

%description -n gstreamer0.10-opencv -l pl.UTF-8
Wtyczka OpenCV do GStreamera. Zawiera następujące elementy:
facedetect, faceblur, edgedetect, cvsobel, cvsmooth, cvlaplace,
cverode, cvequalizehist, cvdilate, textwrite, templatematch,
pyramidsegment.

%package -n gstreamer0.10-opus
Summary:	GStreamer OPUS audio decoder/encoder plugin
Summary(pl.UTF-8):	Wtyczka kodera/dekodera dźwięku OPUS do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Requires:	opus >= 0.9.4
Obsoletes:	gstreamer-opus < 1.0

%description -n gstreamer0.10-opus
GStreamer OPUS audio decoder/encoder plugin.

%description -n gstreamer0.10-opus -l pl.UTF-8
Wtyczka GStreamera kodująca/dekodująca dźwięk w formacie OPUS.

%package -n gstreamer0.10-resindvd
Summary:	GStreamer Resin DVD playback plugin
Summary(pl.UTF-8):	Wtyczka odtwarzania Resin DVD do GStreamera
Group:		Libraries
# for locales
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-resindvd < 1.0

%description -n gstreamer0.10-resindvd
GStreamer Resin DVD playback plugin.

%description -n gstreamer0.10-resindvd -l pl.UTF-8
Wtyczka odtwarzania Resin DVD do GStreamera.

%package -n gstreamer0.10-rtmp
Summary:	RTMP stream input plugin for GStreamer
Summary(pl.UTF-8):	Wtyczka strumieni wejściowych RTMP dla GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-rtmp < 1.0
Conflicts:	gstreamer-plugins-bad < 0.10.22

%description -n gstreamer0.10-rtmp
GStreamer plugin that reads data from a local or remote location
specified by an URI, using any protocol supported by the RTMP library,
i.e. rtmp, rtmpt, rtmps, rtmpe, rtmpfp, rtmpte and rtmpts.

%description -n gstreamer0.10-rtmp -l pl.UTF-8
Wtyczka GStreamera czytająca dane z lokalnego lub zdalnego miejsca
określonego URI przy użyciu dowolnego protokołu obsługiwanego przez
bibliotekę RTMP: rtmp, rtmpt, rtmps, rtmpe, rtmpfp, rtmpte lub rtmpts.

%package -n gstreamer0.10-schroedinger
Summary:	Schroedinger plugin for GStreamer
Summary(pl.UTF-8):	Wtyczka Schroedinger do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Requires:	schroedinger >= 1.0.7
Obsoletes:	gstreamer-schroedinger < 1.0
Obsoletes:	gstreamer-schroedinger = 1.0.7

%description -n gstreamer0.10-schroedinger
Schroedinger plugin for GStreamer.

%description -n gstreamer0.10-schroedinger -l pl.UTF-8
Wtyczka Schroedinger do GStreamera.

%package -n gstreamer0.10-sndfile
Summary:	GStreamer sndfile plugin
Summary(pl.UTF-8):	Wtyczka sndfile do GStreamera
Group:		Libraries
# for locales
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer0.10 >= %{gst_req_ver}
Requires:	libsndfile >= 1.0.16
Obsoletes:	gstreamer-sndfile < 1.0

%description -n gstreamer0.10-sndfile
GStreamer sndfile source plugin.

%description -n gstreamer0.10-sndfile -l pl.UTF-8
Wtyczka sndfile do GStreamera.

%package -n gstreamer0.10-soundtouch
Summary:	GStreamer soundtouch plugin
Summary(pl.UTF-8):	Wtyczka soundtouch do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Requires:	soundtouch >= 1.4
Obsoletes:	gstreamer-soundtouch < 1.0

%description -n gstreamer0.10-soundtouch
GStreamer soundtouch source plugin - audio pitch controller.

%description -n gstreamer0.10-soundtouch -l pl.UTF-8
Wtyczka soundtouch do GStreamera, sterująca wysokością dźwięku.

%package -n gstreamer0.10-spandsp
Summary:	GStreamer SpanDSP plugin
Summary(pl.UTF-8):	Wtyczka SpanDSP do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Requires:	spandsp >= 0.0.6
Obsoletes:	gstreamer-spandsp < 1.0

%description -n gstreamer0.10-spandsp
GStreamer SpanDSP plugin - audio effect that allows packet loss
concealment.

%description -n gstreamer0.10-spandsp -l pl.UTF-8
Wtyczka SpanDSP do GStreamera - efekt dźwiękowy umożliwiający
ukrywanie strat pakietów.

%package -n gstreamer0.10-spc
Summary:	GStreamer SPC plugin
Summary(pl.UTF-8):	Wtyczka SPC dla GStreamera
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Requires:	libopenspc >= 0.3.99
Obsoletes:	gstreamer-spc < 1.0

%description -n gstreamer0.10-spc
GStreamer Plugin for playing SPC files using OpenSPC library.

%description -n gstreamer0.10-spc -l pl.UTF-8
Wtyczka GStreamera odtwarzająca pliki SPC przy użyciu biblioteki
OpenSPC.

%package -n gstreamer0.10-swfdec
Summary:	GStreamer Flash redering plugin
Summary(pl.UTF-8):	Wtyczka renderująca animacje flash dla GStreamera
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Requires:	swfdec >= 0.3.6
Obsoletes:	gstreamer-swfdec < 1.0

%description -n gstreamer0.10-swfdec
Plugin for rendering Flash animations using swfdec library.

%description -n gstreamer0.10-swfdec -l pl.UTF-8
Wtyczka renderująca animacje flash w oparciu o bibliotekę swfdec.

%package -n gstreamer0.10-teletextdec
Summary:	teletextdec plugin for GStreamer
Summary(pl.UTF-8):	Wtyczka teletextdec do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-teletextdec < 1.0

%description -n gstreamer0.10-teletextdec
Teletext decoder plugin for GStreamer.

%description -n gstreamer0.10-teletextdec -l pl.UTF-8
Wtyczka dekodująca teletekst do GStreamera.

%package -n gstreamer0.10-timidity
Summary:	timidity plugin for GStreamer
Summary(pl.UTF-8):	Wtyczka timidity do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-timidity < 1.0

%description -n gstreamer0.10-timidity
timidity plugin for GStreamer.

%description -n gstreamer0.10-timidity -l pl.UTF-8
Wtyczka timidity do GStreamera.

%package -n gstreamer0.10-videosink-sdl
Summary:	GStreamer plugin for outputing to SDL
Summary(pl.UTF-8):	Wtyczka wyjścia SDL do GStreamera
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Provides:	gstreamer0.10-videosink = %{version}
Obsoletes:	gstreamer-SDL
Obsoletes:	gstreamer-videosink-sdl < 1.0

%description -n gstreamer0.10-videosink-sdl
Plugin for sending output to the Simple Direct Media architecture.
<http://www.libsdl.org/). Usefull for fullscreen playback.

%description -n gstreamer0.10-videosink-sdl -l pl.UTF-8
Wtyczka przekazująca wyjście do architektury SDL. Użyteczna do
odtwarzania na pełnym ekranie.

%package -n gstreamer0.10-videosink-directfb
Summary:	GStreamer DirectFB output plugin
Summary(pl.UTF-8):	Wtyczka wyjścia obrazu DirectFB do GStreamera
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Provides:	gstreamer0.10-videosink = %{version}
Obsoletes:	gstreamer-videosink-videosink-directfb < 1.0

%description -n gstreamer0.10-videosink-directfb
GStreamer DirectFB output plugin.

%description -n gstreamer0.10-videosink-directfb -l pl.UTF-8
Wtyczka wyjścia obrazu DirectFB do GStreamera.

%package -n gstreamer0.10-voaacenc
Summary:	AAC encoder plugin for GStreamer
Summary(pl.UTF-8):	Wtyczka kodera dźwięku AAC do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Requires:	vo-aacenc >= 0.1.0
Obsoletes:	gstreamer-videosink-voaacenc < 1.0

%description -n gstreamer0.10-voaacenc
AAC audio encoder plugin for GStreamer using VisualOn library.

%description -n gstreamer0.10-voaacenc -l pl.UTF-8
Wtyczka kodera dźwięku AAC do GStreamera, wykorzystująca bibliotekę
VisualOn.

%package -n gstreamer0.10-vp8
Summary:	GStreamer VP8 encoding and decoding plugin
Summary(pl.UTF-8):	Wtyczka kodująca i dekodująca VP8 dla GStreamera
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Obsoletes:	gstreamer-videosink-vp8 < 1.0

%description -n gstreamer0.10-vp8
GStreamer VP8 encoding and decoding plugin.

%description -n gstreamer0.10-vp8 -l pl.UTF-8
Wtyczka kodująca i dekodująca VP8 dla GStreamera.

%package -n gstreamer0.10-wildmidi
Summary:	wildmidi plugin for GStreamer
Summary(pl.UTF-8):	Wtyczka wildmidi do GStreamera
Group:		Libraries
Requires:	gstreamer0.10 >= %{gst_req_ver}
Obsoletes:	gstreamer-videosink-wildmidi < 1.0

%description -n gstreamer0.10-wildmidi
wildmidi plugin for GStreamer.

%description -n gstreamer0.10-wildmidi -l pl.UTF-8
Wtyczka wildmidi do GStreamera.

%package -n gstreamer0.10-xvid
Summary:	GStreamer xvid decoder plugin
Summary(pl.UTF-8):	Wtyczka do GStreamera dekodująca przy użyciu biblioteki xvid
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Obsoletes:	gstreamer-videosink-xvid < 1.0

%description -n gstreamer0.10-xvid
GStreamer xvid decoder plugin.

%description -n gstreamer0.10-xvid -l pl.UTF-8
Wtyczka do GStreamera dekodująca przy użyciu biblioteki xvid.

%package -n gstreamer0.10-zbar
Summary:	GStreamer ZBar barcode scanner plugin
Summary(pl.UTF-8):	Wtyczka do GStreamera skanująca kody kreskowe
Group:		Libraries
Requires:	gstreamer0.10-plugins-base >= %{gstpb_req_ver}
Requires:	zbar >= 0.9
Obsoletes:	gstreamer-videosink-zbar < 1.0

%description -n gstreamer0.10-zbar
GStreamer ZBar barcode scanner plugin.

%description -n gstreamer0.10-zbar -l pl.UTF-8
Wtyczka do GStreamera skanująca kody kreskowe.

%prep
%setup -q -n %{gstname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_cdaudio:--disable-cdaudio} \
	%{!?with_divx4linux:--disable-divx} \
	%{!?with_dirac:--disable-dirac} \
	%{!?with_dts:--disable-dts} \
	%{!?with_faad:--disable-faad} \
	%{!?with_gsm:--disable-gsm} \
	%{!?with_ladspa:--disable-ladspa} \
	%{!?with_mms:--disable-libmms} \
	%{!?with_mjpegtools:--disable-mpeg2enc} \
	%{!?with_musepack:--disable-musepack} \
	%{!?with_neon:--disable-neon} \
	%{!?with_ofa:--disable-ofa} \
	%{!?with_sdl:--disable-sdl} \
	%{!?with_sdl:--disable-sdltest} \
	%{!?with_spc:--disable-spc} \
	%{!?with_swfdec:--disable-swfdec} \
	%{!?with_amr:--disable-voamrwbenc} \
	%{!?with_xvid:--disable-xvid} \
	--disable-silent-rules \
	--disable-static \
	--enable-experimental \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# We don't need plugins' *.la files
%{__rm} $RPM_BUILD_ROOT%{gstlibdir}/*.la

%find_lang %{gstname}-%{gst_major_ver}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{gstname}-%{gst_major_ver}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{_libdir}/libgstbasecamerabinsrc-%{gst_major_ver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstbasecamerabinsrc-%{gst_major_ver}.so.23
%attr(755,root,root) %{_libdir}/libgstbasevideo-%{gst_major_ver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstbasevideo-%{gst_major_ver}.so.23
%attr(755,root,root) %{_libdir}/libgstcodecparsers-%{gst_major_ver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstcodecparsers-%{gst_major_ver}.so.23
%attr(755,root,root) %{_libdir}/libgstphotography-%{gst_major_ver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstphotography-%{gst_major_ver}.so.23
%attr(755,root,root) %{_libdir}/libgstsignalprocessor-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstsignalprocessor-0.10.so.23
%if %{with vdpau}
%attr(755,root,root) %{_libdir}/libgstvdp-%{gst_major_ver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstvdp-%{gst_major_ver}.so.23
%endif
%attr(755,root,root) %{gstlibdir}/libgstadpcmdec.so
%attr(755,root,root) %{gstlibdir}/libgstadpcmenc.so
%attr(755,root,root) %{gstlibdir}/libgstasfmux.so
%attr(755,root,root) %{gstlibdir}/libgstaudiovisualizers.so
%attr(755,root,root) %{gstlibdir}/libgstautoconvert.so
%attr(755,root,root) %{gstlibdir}/libgstaiff.so
%attr(755,root,root) %{gstlibdir}/libgstapexsink.so
%attr(755,root,root) %{gstlibdir}/libgstbayer.so
%attr(755,root,root) %{gstlibdir}/libgstbz2.so
%attr(755,root,root) %{gstlibdir}/libgstcamerabin.so
%attr(755,root,root) %{gstlibdir}/libgstcamerabin2.so
%attr(755,root,root) %{gstlibdir}/libgstcoloreffects.so
%attr(755,root,root) %{gstlibdir}/libgstcolorspace.so
%attr(755,root,root) %{gstlibdir}/libgstcdxaparse.so
%attr(755,root,root) %{gstlibdir}/libgstcog.so
%attr(755,root,root) %{gstlibdir}/libgstdataurisrc.so
%attr(755,root,root) %{gstlibdir}/libgstdccp.so
%attr(755,root,root) %{gstlibdir}/libgstdtmf.so
%attr(755,root,root) %{gstlibdir}/libgstdebugutilsbad.so
%attr(755,root,root) %{gstlibdir}/libgstdecklink.so
%attr(755,root,root) %{gstlibdir}/libgstdvb.so
%attr(755,root,root) %{gstlibdir}/libgstdvbsuboverlay.so
%attr(755,root,root) %{gstlibdir}/libgstdvdspu.so
%attr(755,root,root) %{gstlibdir}/libgstfaceoverlay.so
%attr(755,root,root) %{gstlibdir}/libgstfbdevsink.so
%attr(755,root,root) %{gstlibdir}/libgstfestival.so
%attr(755,root,root) %{gstlibdir}/libgstfieldanalysis.so
%attr(755,root,root) %{gstlibdir}/libgstfragmented.so
%attr(755,root,root) %{gstlibdir}/libgstfreeverb.so
%attr(755,root,root) %{gstlibdir}/libgstfreeze.so
%attr(755,root,root) %{gstlibdir}/libgstfrei0r.so
%attr(755,root,root) %{gstlibdir}/libgstgaudieffects.so
%attr(755,root,root) %{gstlibdir}/libgstgeometrictransform.so
%attr(755,root,root) %{gstlibdir}/libgsth264parse.so
%attr(755,root,root) %{gstlibdir}/libgsthdvparse.so
%attr(755,root,root) %{gstlibdir}/libgstid3tag.so
%attr(755,root,root) %{gstlibdir}/libgstinterlace.so
%attr(755,root,root) %{gstlibdir}/libgstinter.so
%attr(755,root,root) %{gstlibdir}/libgstivfparse.so
%attr(755,root,root) %{gstlibdir}/libgstjp2k.so
%attr(755,root,root) %{gstlibdir}/libgstjp2kdecimator.so
%attr(755,root,root) %{gstlibdir}/libgstjpegformat.so
%attr(755,root,root) %{gstlibdir}/libgstlegacyresample.so
%attr(755,root,root) %{gstlibdir}/libgstlinsys.so
%attr(755,root,root) %{gstlibdir}/libgstliveadder.so
%attr(755,root,root) %{gstlibdir}/libgstmodplug.so
%attr(755,root,root) %{gstlibdir}/libgstmpegdemux.so
%attr(755,root,root) %{gstlibdir}/libgstmpegpsmux.so
%attr(755,root,root) %{gstlibdir}/libgstmpegtsdemux.so
%attr(755,root,root) %{gstlibdir}/libgstmpegtsmux.so
%attr(755,root,root) %{gstlibdir}/libgstmpegvideoparse.so
%attr(755,root,root) %{gstlibdir}/libgstmve.so
%attr(755,root,root) %{gstlibdir}/libgstmxf.so
%attr(755,root,root) %{gstlibdir}/libgstnsf.so
%attr(755,root,root) %{gstlibdir}/libgstnuvdemux.so
%attr(755,root,root) %{gstlibdir}/libgstpatchdetect.so
%attr(755,root,root) %{gstlibdir}/libgstpcapparse.so
%attr(755,root,root) %{gstlibdir}/libgstpnm.so
%attr(755,root,root) %{gstlibdir}/libgstrawparse.so
%ifarch %{ix86} %{x8664}
%attr(755,root,root) %{gstlibdir}/libgstreal.so
%endif
%attr(755,root,root) %{gstlibdir}/libgstremovesilence.so
%attr(755,root,root) %{gstlibdir}/libgstrfbsrc.so
%attr(755,root,root) %{gstlibdir}/libgstrsvg.so
%attr(755,root,root) %{gstlibdir}/libgstrtpmux.so
%attr(755,root,root) %{gstlibdir}/libgstrtpvp8.so
%attr(755,root,root) %{gstlibdir}/libgstscaletempoplugin.so
%attr(755,root,root) %{gstlibdir}/libgstsdi.so
%attr(755,root,root) %{gstlibdir}/libgstsdpelem.so
%attr(755,root,root) %{gstlibdir}/libgstsegmentclip.so
%attr(755,root,root) %{gstlibdir}/libgstshm.so
%attr(755,root,root) %{gstlibdir}/libgstsiren.so
%attr(755,root,root) %{gstlibdir}/libgstsmooth.so
%attr(755,root,root) %{gstlibdir}/libgststereo.so
%attr(755,root,root) %{gstlibdir}/libgstsubenc.so
%attr(755,root,root) %{gstlibdir}/libgsttta.so
%attr(755,root,root) %{gstlibdir}/libgstvcdsrc.so
%if %{with vdpau}
%attr(755,root,root) %{gstlibdir}/libgstvdpau.so
%endif
%attr(755,root,root) %{gstlibdir}/libgstvideofiltersbad.so
%attr(755,root,root) %{gstlibdir}/libgstvideoparsersbad.so
%attr(755,root,root) %{gstlibdir}/libgstvideomaxrate.so
%attr(755,root,root) %{gstlibdir}/libgstvideosignal.so
%attr(755,root,root) %{gstlibdir}/libgstvideomeasure.so
%attr(755,root,root) %{gstlibdir}/libgstvmnc.so
%attr(755,root,root) %{gstlibdir}/libgsty4mdec.so
%{_gtkdocdir}/gst-plugins-bad-plugins-0.10

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstbasecamerabinsrc-%{gst_major_ver}.so
%attr(755,root,root) %{_libdir}/libgstbasevideo-%{gst_major_ver}.so
%attr(755,root,root) %{_libdir}/libgstcodecparsers-%{gst_major_ver}.so
%attr(755,root,root) %{_libdir}/libgstphotography-%{gst_major_ver}.so
%attr(755,root,root) %{_libdir}/libgstsignalprocessor-%{gst_major_ver}.so
%{_libdir}/libgstbasecamerabinsrc-%{gst_major_ver}.la
%{_libdir}/libgstbasevideo-%{gst_major_ver}.la
%{_libdir}/libgstcodecparsers-%{gst_major_ver}.la
%{_libdir}/libgstphotography-%{gst_major_ver}.la
%{_libdir}/libgstsignalprocessor-%{gst_major_ver}.la
%{_includedir}/gstreamer-0.10/gst/basecamerabinsrc
%{_includedir}/gstreamer-0.10/gst/codecparsers
%{_includedir}/gstreamer-0.10/gst/interfaces/photography-enumtypes.h
%{_includedir}/gstreamer-0.10/gst/interfaces/photography.h
%{_includedir}/gstreamer-0.10/gst/signalprocessor
%{_includedir}/gstreamer-0.10/gst/video/gstbasevideocodec.h
%{_includedir}/gstreamer-0.10/gst/video/gstbasevideodecoder.h
%{_includedir}/gstreamer-0.10/gst/video/gstbasevideoencoder.h
%{_includedir}/gstreamer-0.10/gst/video/gstbasevideoutils.h
%{_includedir}/gstreamer-0.10/gst/video/gstsurfacebuffer.h
%{_includedir}/gstreamer-0.10/gst/video/gstsurfaceconverter.h
%{_includedir}/gstreamer-0.10/gst/video/videocontext.h
%if %{with vdpau}
%attr(755,root,root) %{_libdir}/libgstvdp-%{gst_major_ver}.so
%{_libdir}/libgstvdp-%{gst_major_ver}.la
%{_includedir}/gstreamer-0.10/gst/vdpau
%endif
%{_pkgconfigdir}/gstreamer-basevideo-%{gst_major_ver}.pc
%{_pkgconfigdir}/gstreamer-codecparsers-%{gst_major_ver}.pc
%{_pkgconfigdir}/gstreamer-plugins-bad-%{gst_major_ver}.pc
%{_gtkdocdir}/gst-plugins-bad-libs-0.10

##
## Plugins
##

%if %{with faad}
%files -n gstreamer0.10-aac
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstfaac.so
%attr(755,root,root) %{gstlibdir}/libgstfaad.so
%endif

%if %{with amr}
%files -n gstreamer0.10-amrwbenc
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstvoamrwbenc.so
# dirs should belong to gstreamer or gstreamer-pb?
%dir %{gstdatadir}
%dir %{gstdatadir}/presets
%{gstdatadir}/presets/GstVoAmrwbEnc.prs
%endif

%files -n gstreamer0.10-ass
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstassrender.so

%files -n gstreamer0.10-audio-effects-bad
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstspeed.so

%files -n gstreamer0.10-audiosink-nas
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstnassink.so

%if %{with cdaudio}
%files -n gstreamer0.10-cdaudio
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstcdaudio.so
%endif

%files -n gstreamer0.10-celt
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstcelt.so

%files -n gstreamer0.10-curl
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstcurl.so

%files -n gstreamer0.10-dc1394
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdc1394.so

%if %{with dirac}
%files -n gstreamer0.10-dirac
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdirac.so
%endif

%if %{with divx4linux}
%files -n gstreamer0.10-divx
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdivxdec.so
%attr(755,root,root) %{gstlibdir}/libgstdivxenc.so
%endif

%if %{with dts}
%files -n gstreamer0.10-dts
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdtsdec.so
%endif

%files -n gstreamer0.10-flite
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstflite.so

%files -n gstreamer0.10-gme
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgme.so

%files -n gstreamer0.10-gsettings
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgsettingselements.so
%{_datadir}/glib-2.0/schemas/org.freedesktop.gstreamer-0.10.default-elements.gschema.xml

%if %{with gsm}
%files -n gstreamer0.10-gsm
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgsm.so
%endif

%files -n gstreamer0.10-kate
%defattr(644,root,root,755)
%doc ext/kate/README
%attr(755,root,root) %{gstlibdir}/libgstkate.so

%if %{with ladspa}
%files -n gstreamer0.10-ladspa
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstladspa.so
%endif

%files -n gstreamer0.10-lv2
%defattr(644,root,root,755)
%doc ext/lv2/README
%attr(755,root,root) %{gstlibdir}/libgstlv2.so

%files -n gstreamer0.10-mimic
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstmimic.so

%if %{with mjpegtools}
%files -n gstreamer0.10-mjpegtools
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstmpeg2enc.so
%attr(755,root,root) %{gstlibdir}/libgstmplex.so
%endif

%if %{with mms}
%files -n gstreamer0.10-mms
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstmms.so
%endif

%if %{with musepack}
%files -n gstreamer0.10-musepack
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstmusepack.so
%endif

%files -n gstreamer0.10-musicbrainz
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgsttrm.so

%files -n gstreamer0.10-mythtv
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstmythtvsrc.so

%if %{with neon}
%files -n gstreamer0.10-neon
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstneonhttpsrc.so
%endif

%if %{with ofa}
%files -n gstreamer0.10-ofa
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstofa.so
%endif

%files -n gstreamer0.10-openal
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstopenal.so

%if %{with opencv}
%files -n gstreamer0.10-opencv
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstopencv.so
%endif

%files -n gstreamer0.10-opus
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstopus.so

%files -n gstreamer0.10-resindvd
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libresindvd.so

%files -n gstreamer0.10-rtmp
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstrtmp.so

%files -n gstreamer0.10-schroedinger
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstschro.so

%files -n gstreamer0.10-sndfile
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstsndfile.so

%files -n gstreamer0.10-soundtouch
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstsoundtouch.so

%files -n gstreamer0.10-spandsp
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstspandsp.so

%if %{with spc}
%files -n gstreamer0.10-spc
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstspc.so
%endif

%if %{with swfdec}
%files -n gstreamer0.10-swfdec
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstswfdec.so
%endif

%files -n gstreamer0.10-teletextdec
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstteletextdec.so

%files -n gstreamer0.10-timidity
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgsttimidity.so

%files -n gstreamer0.10-vp8
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstvp8.so

%files -n gstreamer0.10-voaacenc
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstvoaacenc.so

%if %{with sdl}
%files -n gstreamer0.10-videosink-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstsdl.so
%endif

%if %{with directfb}
%files -n gstreamer0.10-videosink-directfb
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdfbvideosink.so
%endif

%%files -n gstreamer0.10-wildmidi
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstwildmidi.so

%if %{with xvid}
%files -n gstreamer0.10-xvid
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstxvid.so
%endif

%files -n gstreamer0.10-zbar
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstzbar.so
