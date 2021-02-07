
"use strict";

let MasterboardDataMsg = require('./MasterboardDataMsg.js');
let IOStates = require('./IOStates.js');
let Digital = require('./Digital.js');
let ToolDataMsg = require('./ToolDataMsg.js');
let RobotStateRTMsg = require('./RobotStateRTMsg.js');
let RobotModeDataMsg = require('./RobotModeDataMsg.js');
let Analog = require('./Analog.js');

module.exports = {
  MasterboardDataMsg: MasterboardDataMsg,
  IOStates: IOStates,
  Digital: Digital,
  ToolDataMsg: ToolDataMsg,
  RobotStateRTMsg: RobotStateRTMsg,
  RobotModeDataMsg: RobotModeDataMsg,
  Analog: Analog,
};
