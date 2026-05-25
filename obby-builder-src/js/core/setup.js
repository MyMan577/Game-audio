// ── Obby Builder V8 - Core Setup & Initialization ──────────────────────────────

import { GRID, WORLD_W, WORLD_H, TILE } from '../constants.js';

export function initCanvas(canvas) {
  const ctx = canvas.getContext('2d');
  let dpr = Math.max(1, Math.min(2, window.devicePixelRatio || 1));
  
  function resize() {
    const rect = canvas.parentElement.getBoundingClientRect();
    canvas.width = Math.floor(rect.width * dpr);
    canvas.height = Math.floor(rect.height * dpr);
    ctx.scale(dpr, dpr);
  }
  
  resize();
  window.addEventListener('resize', resize);
  
  return { ctx, resize };
}

export function initGameArea() {
  return {
    grid: GRID,
    worldWidth: WORLD_W,
    worldHeight: WORLD_H,
    tile: TILE
  };
}
