/**************************************************************************
 * Copyright 2015 Sensel, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 * http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 **************************************************************************/

#ifndef SENSEL_TYPES_H
#define SENSEL_TYPES_H

// TODO: We may not want to define any of these types in our library
// to maintain maximum compatibility with external code

#ifdef WIN32
  #ifndef __cplusplus
    #define false (0)
    #define true  (1)
    #define bool unsigned char
  #endif
#else
#include <stdbool.h>
#endif
     
typedef unsigned char uint8;
typedef unsigned short uint16;
typedef unsigned int uint32;
typedef unsigned long long int uint64;

typedef char int8;
typedef short int16;
typedef int int32;
typedef long long int int64;


#endif //SENSEL_TYPES_H
