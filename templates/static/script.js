const chatBody = document.getElementById("chatBody");
const userInput = document.getElementById("userInput");
const sendBtn = document.getElementById("sendBtn");

function addMessage(message, type) {
    const messageDiv = document.createElement("div");

    messageDiv.classList.add("message", type);
    messageDiv.textContent = message;

    chatBody.appendChild(messageDiv);
    chatBody.scrollTop = chatBody.scrollHeight;
}

async function sendMessage() {
    const message = userInput.value.trim();

    if (message === "") {
        return;
    }

    addMessage(message, "user-message");
    userInput.value = "";

    sendBtn.disabled = true;
    sendBtn.textContent = "Sending...";

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.reply || "Something went wrong");
        }

        addMessage(data.reply, "bot-message");

    } catch (error) {
        addMessage(
            "Sorry! Server se connection nahi ho pa raha. Please try again.",
            "bot-message"
        );

        console.error(error);

    } finally {
        sendBtn.disabled = false;
        sendBtn.textContent = "Send ➤";
        userInput.focus();
    }
}

function sendQuickMessage(message) {
    userInput.value = message;
    sendMessage();
}

userInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});