/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./templates/**/*.html",
        "./static/**/*.js",
    ],
    theme: {
        extend: {
            colors: {
                'primary': '#3490dc',
                'secondary': '#ffed4a',
            },
            fontFamily: {
                'sans': ['Ubuntu', 'sans-serif'],
            },
        },
    },
    plugins: [],
}