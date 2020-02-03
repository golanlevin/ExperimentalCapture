#include <exception>
#include <mutex>

#include "sensel.h"

class ofxSenselMorph {
 public:
  static const int defaultFlags = SENSEL_FRAME_CONTENT_PRESSURE_MASK;

  ofxSenselMorph(int initFlags = ofxSenselMorph::defaultFlags)
      : _flags(initFlags) {
    bool ok = senselOpenConnection(nullptr);
    if (!ok) {
      throw std::runtime_error("ofxSenselMorph: could not open connection");
    }
    init(initFlags);
  }

  ofxSenselMorph(std::string com_port,
                 int initFlags = ofxSenselMorph::defaultFlags)
      : _flags(initFlags) {
    bool ok = senselOpenConnection(const_cast<char*>(com_port.c_str()));
    if (!ok) {
      throw std::runtime_error("ofxSenselMorph: could not open connection");
    }
    init(initFlags);
  }

  ofxSenselMorph(const ofxSenselMorph& other_copy_ctor) = delete;
  ofxSenselMorph& operator=(const ofxSenselMorph& other_copy_assign) = delete;
  ofxSenselMorph& operator=(ofxSenselMorph&& other) = delete;
  ofxSenselMorph(ofxSenselMorph&& other_move_ctor) = delete;

  ~ofxSenselMorph() {
    if (_inited) {
      close();
    }
  }

  bool opened() { return _inited; };

  void close() {
    senselSetLEDBrightnessAll(0);
    senselStopScanning();
    senselCloseConnection();
  }

  int flags() { return _flags; };

  void update() {
    std::lock_guard<std::mutex> lock(mut);
    senselReadFrame(&_contacts, &_n_contacts, &_forces, &_labels);
  }

  std::vector<uint8_t> labels() {
    return std::vector<uint8_t>(_labels, _labels + n_contacts());
  }

  std::vector<contact_t> contacts() {
    return std::vector<contact_t>(_contacts, _contacts + n_contacts());
  }

  std::vector<std::pair<uint8_t, contact_t> > labeledContacts() {
    std::vector<std::pair<uint8_t, contact_t> > out;
    for (size_t i = 0; i < _n_contacts; i++) {
      out.push_back(std::make_pair(_labels[i], _contacts[i]));
    }
    return out;
  }

  std::vector<float> forces() {
    return std::vector<float>(_forces, _forces + rows() * cols());
  }

  template <class output_iterator>
  void forces(output_iterator& out) {
    std::copy(_forces, _forces + rows() * cols(), out.begin());
  }

  void led(unsigned int i, uint8_t brightness) {
    std::lock_guard<std::mutex> lock(mut);
    senselSetLEDBrightness(i, brightness);
  }

  /* rawDataArrays : gives you internal data arrays */
  std::tuple<contact_t*, float*, uint8_t*> rawDataArrays() {
    return std::make_tuple(_contacts, _forces, _labels);
  }

  size_t rows() const { return _rows; };

  size_t cols() const { return _cols; };

  size_t n_contacts() const { return _n_contacts; };

 private:
  std::mutex mut;
  bool _inited = false;
  int _flags;
  size_t _rows;
  size_t _cols;
  contact_t* _contacts;
  float* _forces;
  uint8_t* _labels;
  int _n_contacts = 0;

  void init(int initFlags) {
    std::lock_guard<std::mutex> lock(mut);

    senselSetFrameContentControl(initFlags);
    _cols = senselDecompressGetCols();
    _rows = senselDecompressGetRows();
    senselStartScanning();
    _inited = true;
  }
};
