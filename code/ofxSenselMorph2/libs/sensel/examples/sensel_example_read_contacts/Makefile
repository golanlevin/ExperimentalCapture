# Program name
PROGRAM = sensel_example_read_contacts

# Setup directories here
SENSEL_DIR = ../..
SOURCE_DIR = .
INCLUDE_DIR = 
BUILD_DIR = build
LIB_DIR = .
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
    LIBS = ./libSensel.so
endif
ifeq ($(UNAME_S),Darwin)
	LIBS = ./libSensel.dylib
endif
# Add user files here
CXX_SOURCES = 
C_SOURCES = main.c

##### Careful editing below this line! #####

SENSEL_SOURCES += sensel.c sensel_serial_linux.c
INCLUDE_DIRS += -I $(SENSEL_DIR)

OS := $(shell uname)

OPTIMIZATIONS = -O3
CXXFLAGS = ${DEFINES} ${OPTIMIZATIONS} -Wall -g  $(INCLUDE_DIRS) 
CFLAGS = ${DEFINES} ${OPTIMIZATIONS} -Wall -g -std=gnu99 $(INCLUDE_DIRS)

# expands to list of object files
CXX_OBJS = $(addprefix $(BUILD_DIR)/,$(CXX_SOURCES:.cpp=.o))
C_OBJS = $(addprefix $(BUILD_DIR)/,$(C_SOURCES:.c=.o))
SENSEL_OBJS = $(addprefix $(BUILD_DIR)/,$(SENSEL_SOURCES:.c=.o))

CXX = g++
CC = gcc

LD_FLAGS = $(LIB_DIRS) $(LIBS)

.PHONY: all clean run

all: $(PROGRAM)

create_path:
	mkdir -p $(BUILD_DIR)

$(BUILD_DIR)/%.o : $(SOURCE_DIR)/%.cpp create_path
	$(CXX) $(CXXFLAGS) -c -o $@ $<

$(BUILD_DIR)/%.o : $(SOURCE_DIR)/%.c create_path
	$(CC) $(CFLAGS) -c -o $@ $<

$(BUILD_DIR)/%.o : $(SENSEL_DIR)/%.c create_path
	$(CC) $(CFLAGS) -c -o $@ $<

$(PROGRAM): $(CXX_OBJS) $(C_OBJS) $(SENSEL_OBJS)
	$(CXX) $(CXXFLAGS) $^ $(LD_FLAGS) -o $@ 

clean:
	$(RM) -rf $(BUILD_DIR) $(PROGRAM)

run:
	./$(PROGRAM) 
