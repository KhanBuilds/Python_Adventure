// File: game.js

const output = document.getElementById("game-output");
const input = document.getElementById("player-input");
const button = document.getElementById("submit-btn");

let gameState = "mainMenu";
let inventory = [];

function display(text) {
  output.textContent += text + "\n\n";
  output.scrollTop = output.scrollHeight;
}

function clear() {
  output.textContent = "";
}

function displayMainMenu() {
  clear();
  gameState = "mainMenu";
  display("------------------------------------------------------------\nWELCOME TO THE GAME\nPRESS S TO START\n------------------------------------------------------------");
}

function startGame() {
  gameState = "intro";
  clear();
  display("Your journey starts in your village...\nYou hear about the heart of gold which controls the fate of the village\n\nWhat do you do next?\n(A) Inquire more about the heart of gold\n(B) Go to the forest without inquiring");
}

function gameOver(text) {
  display(text || "GAME OVER");
  gameState = "mainMenu";
}

function handleInput(inputValue) {
  const choice = inputValue.trim().toUpperCase();

  switch (gameState) {
    case "mainMenu":
      if (choice === "S") {
        startGame();
      } else {
        display("Invalid input. Press 'S' to start.");
      }
      break;

    case "intro":
      if (choice === "A") {
        gameState = "inquireQuest";
        display("Elder: If I tell you, do you take the responsibility of bringing it to us? (A) Yes (B) No");
      } else if (choice === "B") {
        gameState = "forestWithoutInquiry";
        display("You decide to head straight into the forest...\nDo you continue walking into the forest? (Y/N)");
      } else {
        display("Invalid input. Please choose A or B.");
      }
      break;

    case "inquireQuest":
      if (choice === "A") {
        inventory = ["Protective shield", "Invisibility cloak", "Food and Water", "Map of the Gold Castle"];
        gameState = "inquireBattle";
        display("Elder gives you items.\nInventory: " + inventory.join(", ") + "\n\nYou venture into the forest. A Glimmerghost appears!\nUse 'U' to activate Protective Shield.");
      } else if (choice === "B") {
        gameState = "forestWithoutInquiry";
        display("You chose not to inquire. You walk into the forest at night. Do you continue? (Y/N)");
      } else {
        display("Invalid input. Choose A or B.");
      }
      break;

    case "inquireBattle":
      if (choice === "U") {
        display("Shield deflects the Glimmerghost! You stab it. It collapses.\n\nYou continue and arrive at the Golden Castle. Use 'W' to wear the Invisibility Cloak.");
        gameState = "goldenCastleWithCloak";
      } else {
        display("You hesitated. It attacks, but shield burns it. You survive.\nContinue and arrive at the Golden Castle. Use 'W' to wear the Invisibility Cloak.");
        gameState = "goldenCastleWithCloak";
      }
      break;

    case "goldenCastleWithCloak":
      if (choice === "W") {
        display("Cloak worn. Shield drops. You may now touch the Heart of Gold. Press 'T' to touch.");
        gameState = "touchHeartSafe";
      } else {
        display("Invalid. Press 'W' to wear cloak.");
      }
      break;

    case "touchHeartSafe":
      if (choice === "T") {
        display("Brilliant light surrounds you. You’re back in your village.\nThe elder smiles: ‘You have done it!’\nYou’re hailed a hero. THE END.");
        gameState = "mainMenu";
      } else {
        display("Invalid. Press 'T' to touch.");
      }
      break;

    case "forestWithoutInquiry":
      if (choice === "Y") {
        gameState = "forestBattle";
        inventory = ["Knife", "Invisible Vision Potion", "Map of the Gold Castle", "Food", "Water"];
        display("A Glimmerghost appears! Press 'I' to check inventory.");
      } else if (choice === "N") {
        gameState = "goBackVillage";
        display("You return to village and talk to the elder... Proceed as if you chose to inquire. Press 'A' to accept quest.");
      } else {
        display("Invalid input. Choose Y or N.");
      }
      break;

    case "forestBattle":
      if (choice === "I") {
        display("Inventory: " + inventory.join(", ") + "\nChoose 1 for Knife, 2 for Potion");
        gameState = "chooseWeapon";
      } else {
        display("Invalid. Press 'I' to check inventory.");
      }
      break;

    case "chooseWeapon":
      if (choice === "1") {
        gameState = "ending2";
        display("You stab the invisible ghost with instinct. It flees. You rest. Then you are killed in sleep. THE END.");
      } else if (choice === "2") {
        gameState = "restDecision";
        display("You drink potion, kill ghost. Rest? (Y/N)");
      } else {
        display("You die. Wrong choice. THE END.");
        gameState = "mainMenu";
      }
      break;

    case "restDecision":
      if (choice === "Y") {
        gameState = "castleWithoutElder";
        display("You rest, then walk to castle. Use 'M' to pull out map.");
      } else if (choice === "N") {
        gameState = "castleWithoutElder";
        display("You walk straight to castle. Use 'M' to pull out map.");
      } else {
        display("Invalid input. Y or N.");
      }
      break;

    case "castleWithoutElder":
      if (choice === "M") {
        gameState = "touchHeartNoElder";
        display("Map shows chamber. You reach it. Press 'T' to touch Heart of Gold.");
      } else {
        display("Invalid. Press 'M' to use map.");
      }
      break;

    case "touchHeartNoElder":
      if (choice === "T") {
        display("You touch it without guidance. Intense pain. You die. THE END.");
        gameState = "mainMenu";
      } else {
        display("Invalid. Press 'T' to touch.");
      }
      break;

    case "goBackVillage":
      if (choice === "A") {
        gameState = "inquireQuest";
        display("You accept elder’s quest. Proceeding...");
      } else {
        display("GAME OVER.");
        gameState = "mainMenu";
      }
      break;

    default:
      display("Invalid state or input. Restarting...");
      displayMainMenu();
      break;
  }
}

button.addEventListener("click", () => {
  const value = input.value;
  input.value = "";
  handleInput(value);
});

displayMainMenu();
