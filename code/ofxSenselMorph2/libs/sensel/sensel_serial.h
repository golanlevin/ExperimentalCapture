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

#pragma once

#include "sensel.h"

#ifdef __cplusplus
extern "C" {
#endif

bool senselSerialOpen            (sensel_serial_data *data, char* com_port);
bool senselSerialWrite           (sensel_serial_data *data, uint8* buf, int buf_len);
int  senselSerialReadAvailable   (sensel_serial_data *data, uint8* buf, int buf_len);
bool senselSerialReadBytes       (sensel_serial_data *data, uint8* buf, int buf_len);
int  senselSerialGetAvailable    (sensel_serial_data *data); // Checks number of available bytes
void senselSerialFlushInput      (sensel_serial_data *data);
void senselSerialClose           (sensel_serial_data *data);

#ifdef __cplusplus
}
#endif
