# Svelte for Noobs

Svelte is a modern JavaScript framework that has been gaining popularity for its simplicity and performance. Unlike other frameworks like React or Vue, Svelte shifts much of the work to compile time, resulting in faster runtime performance and smaller bundle sizes. If you're new to Svelte, here's a beginner-friendly guide to get you started.

## Why Svelte?

Svelte stands out because it eliminates the need for a virtual DOM. Instead of diffing and patching the DOM at runtime, Svelte compiles your components into highly efficient imperative code that updates the DOM directly. This approach leads to faster updates and smaller JavaScript bundles.

## Getting Started with Svelte

To start using Svelte, you can create a new project using the official template. Here’s how you can set it up:

```bash
npx degit sveltejs/template svelte-app
cd svelte-app
npm install
npm run dev
```