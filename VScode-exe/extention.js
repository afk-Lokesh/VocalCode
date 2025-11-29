const vscode = require('vscode');
const fetch = require('node-fetch');

function activate(context) {
    console.log('VISOR Activated!');

    let disposable = vscode.commands.registerCommand('visor.start', async function () {
        vscode.window.showInformationMessage('VISOR is listening...');
        await fetch('http://localhost:8000/start_listening');
    });

    context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = { activate, deactivate };
