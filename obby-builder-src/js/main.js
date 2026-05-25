// ── Obby Builder V8 - Main Entry Point ──────────────────────────────

import { initCanvas, initGameArea } from './core/setup.js';
import { PALETTE, CHARACTERS, ENEMY_TYPES } from './constants.js';

// Initialize canvas and game area
const canvas = document.getElementById('c');
const { ctx, resize } = initCanvas(canvas);
const gameArea = initGameArea();

console.log('Obby Builder V8 initialized');
console.log('Canvas context:', ctx);
console.log('Game area:', gameArea);
console.log('Available characters:', CHARACTERS.length);
console.log('Enemy types:', ENEMY_TYPES.length);

// TODO: Import and initialize remaining modules
// - Player controller
// - Building system
// - Enemy AI
// - Physics engine
// - Render loop
// - Input handling
// - Save/load system
