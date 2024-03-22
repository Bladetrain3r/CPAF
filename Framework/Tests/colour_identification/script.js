// This array will hold the 'correct' colors for the squares
// Generate 8 shades of red, evenly spaced from a dark red (R=25) to full red (R=255)
// Currently doesn't compare selected and correct colors properly

const sessionColorBlindnessLevel = 0; // No color blindness effect
const sessionLightLevel = ((0.5 * Math.random()) + 0.5).toFixed(4); // Full opacity
const sessionId = Math.random().toString(36).substr(2, 9); // Generate a random session ID

const correctColors = [];
for (let i = 0; i < 8; i++) {
    // Calculate the red value for the shade
    const redValue = 25 + (i * (255 - 25) / (8 - 1));
    // Create the RGB string for the shade
    const color = `rgb(${Math.round(redValue)},0,0)`;
    // Add the color to the array
    correctColors.push(color);
}

console.log(correctColors); // This will log the array of red shades


// Function to randomize color value considering color blindness level
function getRandomColorValue(colorBlindnessLevel, color) {
    // Parse the red value from the provided RGB string
    const redValue = parseInt(color.slice(4, -1).split(',')[0]);
    // Adjust the red component based on color blindness level
    const adjustedRed = redValue * (1 - colorBlindnessLevel);
    // Return the adjusted color as an RGB string
    return `rgb(${Math.round(adjustedRed)},0,0)`;
}


// Function to display a new square with applied color blindness and light level
function displayNewSquareRapidChanges() {
    const container = document.getElementById('selected-square-container');
    container.innerHTML = ''; // Clear the previous square

    // Randomize the index for the correct color square to be identified
    const correctIndex = (correctIndex + Math.round(Math.random()*8) ) % correctColors.length;
    // Store the 'correct' color
    const correctColor = correctColors[correctIndex];

    // Apply the color blindness and light level alterations to the correct color
    const colorBlindnessLevel = ((0.25 * Math.random()) + 0.75).toFixed(4); // Random color blindness level for demonstration
    const lightLevel = ((0.5 * Math.random()) + 0.5).toFixed(4); // Random light level for demonstration
    const alteredColor = getRandomColorValue(colorBlindnessLevel, correctColor); // Alter the color

    // Create and display the new square with the altered color
    const newSquare = document.createElement('div');
    newSquare.className = 'red-square';
    newSquare.style.backgroundColor = alteredColor;
    newSquare.style.opacity = lightLevel.toString(); // Simulate light level by adjusting opacity
    container.appendChild(newSquare);

    // For debug purposes: display the index of the correct square
    const debugInfo = document.getElementById('debug-info');
    if (!debugInfo) {
        const debugElement = document.createElement('div');
        debugElement.id = 'debug-info';
        document.body.appendChild(debugElement);
    }
    document.getElementById('debug-info').textContent = `Debug: Correct square index is ${correctIndex}`;
}

function displayNewSquare() {
    const container = document.getElementById('selected-square-container');
    container.innerHTML = ''; // Clear the previous square

    // Randomize the index for the correct color square to be identified
    correctIndex = (correctIndex + Math.round(Math.random()*8) ) % correctColors.length;

    const correctColor = correctColors[correctIndex];

    // Use the static session values for color blindness and light level
    const alteredColor = getRandomColorValue(sessionColorBlindnessLevel, correctColor);

    // Create and display the new square with the altered color
    const newSquare = document.createElement('div');
    newSquare.className = 'red-square';
    newSquare.style.backgroundColor = alteredColor;
    newSquare.style.opacity = sessionLightLevel.toString(); // Full opacity for testing
    container.appendChild(newSquare);

    // Update debug information with the new correct index
    updateDebugInfo(correctIndex);
}

// Function to update debug information
function updateDebugInfo(correctIndex) {
    let debugInfo = document.getElementById('debug-info');
    if (!debugInfo) {
        debugInfo = document.createElement('div');
        debugInfo.id = 'debug-info';
        document.body.appendChild(debugInfo);
    }
    // debugInfo.textContent = `Debug: Correct square index is ${correctIndex}`;
    debugInfo.textContent = `Please Select the correct square`;
}

// Initialize correctIndex globally
let correctIndex = -1; // Start at -1 so the first displayed square has index 0

function generateReferenceSquares() {
    const container = document.getElementById('red-squares-container');
    container.innerHTML = ''; // Clear previous content

    // Generate reference squares
    for (let i = 0; i < 8; i++) {
        const refSquare = document.createElement('div');
        refSquare.className = 'red-square';
        refSquare.dataset.color = i; // Data attribute to identify the square
        refSquare.style.backgroundColor = correctColors[i];
        container.appendChild(refSquare);
    }
}

// Event delegation for clicks on reference squares
document.getElementById('red-squares-container').addEventListener('click', function(event) {
    if (event.target.className === 'red-square') {
        handleSelection(event.target.dataset.color);
    }
});


// Function to handle user selection
function handleSelection(selectedColorIndex) {
    selectedColorIndex = parseInt(selectedColorIndex);

    // Check if the selected index matches the correct index
    const correct = selectedColorIndex === correctIndex;

    // Retrieve the altered color for the selected square
    const selectedColor = correctColors[selectedColorIndex];

    // Retrieve the session data from local storage or initialize it if not present
    let sessionData = JSON.parse(localStorage.getItem('sessionData')) || [];

    // Record the attempt
    sessionData.push({
        selectedColor: selectedColor,
        correct: correct,
        baseColor: correctColors[correctIndex],
        alterations: {
            colorBlindnessLevel: sessionColorBlindnessLevel,
            lightLevel: sessionLightLevel
        }
    });

    // Save the attempt to local storage
    localStorage.setItem('sessionData', JSON.stringify(sessionData));

    // If 10 attempts are reached, present summary and offer data download
    if (sessionData.length >= 10) {
        presentSummaryAndDownload(sessionData);
    } else {
        // Otherwise, display a new square
        displayNewSquare();
    }
}

function downloadResults(sessionData) {
    // Prepare data for download

    const dataToDownload = sessionData.map((data, index) => ({
        attempt: index + 1,
        baseColor: correctColors[index], // assuming correctColors is accessible and in sync
        selectedColor: data.selectedColor,
        wasCorrect: data.correct,
        alterations: {
            colorBlindnessLevel: data.colorBlindnessLevel, // Need to store this for each attempt if fully randomised
            lightLevel: data.lightLevel // Need to store this for each attempt if fully randomised
        }
    }));

    // Prepend light level and color blindness level to the data
    dataToDownload.unshift({
        lightLevel: sessionLightLevel,
        colorBlindnessLevel: sessionColorBlindnessLevel
    });

    // Prepend the session ID to the data
    dataToDownload.unshift({ sessionId: sessionId });


    // Convert data to JSON format
    const json = JSON.stringify(dataToDownload, null, 2);
    const blob = new Blob([json], { type: 'application/json' });
    const url = URL.createObjectURL(blob);

    // Create a link and download the file
    const a = document.createElement('a');
    a.href = url;
    a.download = 'session-results.json';
    a.click();

    // Clean up URL
    URL.revokeObjectURL(url);
}

function presentSummaryAndDownload(sessionData) {
    let correctCount = sessionData.filter(entry => entry.correct).length;
    alert(`Session complete! Your accuracy was ${correctCount / sessionData.length * 100}%`);
    downloadResults(sessionData);

    // Clear the session data
    localStorage.removeItem('sessionData');
    // Also reset any session-related states if necessary, e.g., correctColors array
    correctColors.length = 0; // If you use this array to store session color data
    // Reloading the page to reset the state and start a new session
    window.location.reload();
}

// Ensure displayNewSquare is called as soon as the window loads
window.onload = function() {
    generateReferenceSquares();
    displayNewSquare();
};
