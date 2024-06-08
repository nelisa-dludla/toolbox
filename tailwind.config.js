/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
	'./toolbox_workshop/templates/toolbox_workshop/*.html',
  ],
  theme: {
    extend: {
		colors: {
			'toolbox-green': '#255957',
			'toolbox-hover-green': '#428684',
		},
	},
  },
  plugins: [],
}

