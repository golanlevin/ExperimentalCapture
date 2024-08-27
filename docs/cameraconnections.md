# Camera Connections

[Axis Camera Info - permission required, student access only.](https://docs.google.com/document/d/1JhGlfEX-YZKQIJL193PoBLZXpsM68H6zVT81oVtsrCY/edit?usp=sharing)

## Video Output Connections for Cameras

- **HDMI (High-Definition Multimedia Interface)**
  - Mini HDMI or Micro HDMI: Common in consumer and some professional cameras for external video monitors or recorders.

- **SDI (Serial Digital Interface)**
  - BNC connectors, typically used in professional video cameras, for high-quality video output over longer distances.

- **USB (Universal Serial Bus)**
  - USB 2.0/3.0/Type-C: Found on many modern cameras for streaming video or file transfer to computers or other devices.

- **AV (Analog Video)**
  - Composite or Component connections: Older cameras often use RCA cables or YPbPr for analog video signals.

- **FireWire (IEEE 1394)**
  - Found in some older video cameras for digital video transfer, particularly common with miniDV camcorders.

- **Ethernet**
  - Network connections for IP cameras or live streaming via direct network transfer.

- **Wi-Fi / Wireless Output**
  - Some cameras support wireless video output for live streaming or direct transfer to mobile devices.

- **XLR / Balanced Video Outputs**
  - Rare, but occasionally seen in professional or industrial video systems.

---

## Video Formats Carried Over Ethernet

- **RTSP (Real-Time Streaming Protocol)**
  - Standard for real-time streaming of audio and video over IP networks.
  - Common formats: H.264, H.265, MJPEG.

- **NDI (Network Device Interface)**
  - A video-over-IP protocol developed by NewTek, used for low-latency, high-quality video transmission over Ethernet.
  - Supports up to 4K resolution and various formats like H.264, H.265, and ProRes.

- **SRT (Secure Reliable Transport)**
  - Designed for low-latency, secure video streaming over the internet or IP networks.
  - Formats typically include H.264 and H.265.

- **HLS (HTTP Live Streaming)**
  - Common streaming protocol for delivering video over Ethernet, often used for adaptive bitrate streaming.
  - Formats: H.264, H.265.

- **MPEG-TS (Transport Stream)**
  - Used for streaming video over IP, often used in broadcasting.
  - Formats: H.264, H.265, MPEG-2.

- **Dante AV**
  - Protocol for carrying video (along with audio) over IP networks, developed by Audinate.
  - Video formats: H.264, H.265.

- **JPEG XS**
  - A low-latency, lightweight video compression format used in professional video transmission over IP networks.
  - Common in broadcast and live event production.

- **IPTV (Internet Protocol Television)**
  - Streaming video to set-top boxes or apps over Ethernet, often using H.264 or H.265 formats.

- **ONVIF**
  - A standard used for video over IP, particularly in security cameras.
  - Formats typically include H.264 and H.265.

- **Pro AV over IP**
  - Formats for video signals over Ethernet used in professional AV environments, supporting uncompressed video transmission.
  - Formats: SDVoE (Software Defined Video over Ethernet), AVB/TSN.

- **WebRTC (Web Real-Time Communication)**
  - Real-time communication protocol for video and audio over IP.
  - Formats: VP8, VP9, H.264.

- **RTMP (Real-Time Messaging Protocol)**
  - Protocol for transmitting video streams over IP.
  - Formats: Typically H.264 and H.265.

- **Zixi**
  - Professional video streaming protocol, used in broadcast-grade streaming over IP.
  - Formats: H.264, H.265.

- **RTP (Real-time Transport Protocol)**
  - Used for delivering real-time video and audio over IP networks.
  - Formats: H.264, H.265, VP8, VP9.

## Difference Between RTSP and NDI

### **RTSP (Real-Time Streaming Protocol)**

- **Purpose:** RTSP is primarily used for controlling and delivering real-time streaming media over IP networks. It is a client-server protocol designed for communication and controlling the streaming of audio and video, commonly used in IP cameras, media servers, and online streaming services.
  
- **Latency:** RTSP typically has higher latency compared to protocols like NDI, often in the range of hundreds of milliseconds to a few seconds. This is because it is usually used for video streaming over the internet or large networks where buffering is common to ensure smooth playback.
  
- **Compression Formats:** RTSP streams video in formats like H.264, H.265, or MJPEG, relying heavily on compression to minimize bandwidth use. This makes it suitable for streaming over the internet or lower-bandwidth networks.
  
- **Use Cases:** RTSP is widely used for video surveillance, IP cameras, and video-on-demand services. It's often integrated into systems where real-time control is needed, but ultra-low latency is not critical.
  
- **Network Requirements:** RTSP is often used over TCP or UDP, and depending on the application, it might require a stable connection to ensure video quality. Its performance may degrade over unreliable or congested networks.

### **NDI (Network Device Interface)**

- **Purpose:** NDI is a protocol developed by NewTek for transmitting high-quality, low-latency video and audio over standard IP networks. It is designed for professional broadcast and production environments, enabling multiple video streams to be sent over a local area network (LAN) with minimal latency.
  
- **Latency:** NDI is designed for ultra-low latency, typically under one frame of delay, making it ideal for live production environments where timing is crucial. It is often used in situations where real-time interaction with video is necessary, such as live streaming, video mixing, and broadcast.
  
- **Compression Formats:** NDI uses a high-efficiency codec that supports compressed but visually lossless video, often at high resolutions (up to 4K) and frame rates. The compression is optimized to maintain high quality while minimizing network load, and uncompressed video is also supported.
  
- **Use Cases:** NDI is widely used in live broadcasting, video production studios, live events, and any environment where multiple video sources need to be switched, mixed, or transmitted with minimal delay. It is increasingly used in hybrid workflows that combine local and remote production.
  
- **Network Requirements:** NDI works best over a stable, high-bandwidth LAN environment, often requiring gigabit Ethernet or higher for smooth operation. It is designed to efficiently use available network resources while maintaining quality, but it may not perform as well over low-bandwidth or unreliable networks.

### **Summary:**

- **RTSP** invented in 1996, is optimized for delivering compressed video over the internet with higher latency and is more commonly used in IP cameras and streaming applications where real-time interaction isn't critical.
- **NDI** invented in 2015, focuses on high-quality, low-latency video over local networks, ideal for live production and broadcast where minimal delay is essential.
