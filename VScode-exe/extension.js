const vscode = require("vscode");
const { spawn } = require("child_process");

function activate(context) {

    let disposable = vscode.commands.registerCommand("visor.start", function () {
        vscode.window.showInformationMessage("VISOR is starting...");

        const listener = spawn("python", [
            "backend/speech/listener.py"
        ]);

        listener.stdout.on("data", (data) => {
            console.log(`VISOR: ${data}`);
        });

        listener.stderr.on("data", (data) => {
            console.error(`VISOR ERROR: ${data}`);
        });
    });

    context.subscriptions.push(disposable);
}
exports.activate = activate;
