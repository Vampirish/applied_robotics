import { Go1, Go1Mode } from "@droneblocks/go1-js";


const MyRobotDog = new Go1({host: "192.168.171.20"});
MyRobotDog.init()

MyRobotDog.setLedColor(255, 0, 0);
await MyRobotDog.wait(1000);
console.log("color set");

await MyRobotDog.setMode(Go1Mode.standUp);
console.log("stand");
await MyRobotDog.wait(3000);

await MyRobotDog.setMode(Go1Mode.walk);
console.log("walk");
await MyRobotDog.wait(3000);

await MyRobotDog.goForward(0.25, 2000);
// MyRobotDog.setMode(Go1Mode.standUp);
// await MyRobotDog.wait(3000);
MyRobotDog.setLedColor(0, 255, 0);
await MyRobotDog.wait(1000);
console.log("color set");

MyRobotDog.setLedColor(0, 0, 255);
await MyRobotDog.wait(1000);
console.log("color set");

// MyRobotDog.goForward(0.25, 2000);
console.log("DOne");