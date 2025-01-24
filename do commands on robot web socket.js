import { Go1, Go1Mode } from "@droneblocks/go1-js";
import WebSocket from "ws";
import {WebSocketServer} from "ws";

const MyRobotDog = new Go1({ host: "192.168.171.20" });
await MyRobotDog.init();

// Map commands to robot actions
const COMMAND_ACTIONS = {
    goForward: async () => {
        await MyRobotDog.goForward(0.25, 2000);
        console.log("Robot moving forward");
    },
    walk: async () => {
        await MyRobotDog.setMode(Go1Mode.walk);
        console.log("Robot walking");
    },
    goBackward: async () => {
        await MyRobotDog.goBackward(0.25, 2000);
        console.log("Robot moving backward");
    },
    turnLeft: async () => {
        await MyRobotDog.turnLeft(0.5, 1000);
        console.log("Robot turning left");
    },
    turnRight: async () => {
        await MyRobotDog.turnRight(0.5, 1000);
        console.log("Robot turning right");
    },
    stop: async () => {
        await MyRobotDog.setMode(Go1Mode.standUp);
        console.log("Robot stopped");
    },
};

// Start WebSocket server
const wss = new WebSocketServer({ port: 8765 });

wss.on("connection", (ws) => {
    console.log("Python connected to WebSocket");

    ws.on("message", async (message) => {
        const command = message.toString();
        console.log(`Received command: ${command}`);

        const action = COMMAND_ACTIONS[command];
        if (action) {
            await action();
        } else {
            console.log(`Unknown command: ${command}`);
        }
    });
});

console.log("WebSocket server is running on ws://localhost:8765");
