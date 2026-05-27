const fs = require('fs');

async function fetchMenu() {
    try {
        const response = await fetch('https://darbarseafoodrestaurant.vercel.app/menu.html');
        const text = await response.text();
        fs.writeFileSync('darbar_menu.html', text);
        console.log('Saved darbar_menu.html');
        
        const cssResponse = await fetch('https://darbarseafoodrestaurant.vercel.app/style.css');
        const cssText = await cssResponse.text();
        fs.writeFileSync('darbar_style.css', cssText);
        console.log('Saved darbar_style.css');
        
        const jsResponse = await fetch('https://darbarseafoodrestaurant.vercel.app/script.js');
        const jsText = await jsResponse.text();
        fs.writeFileSync('darbar_script.js', jsText);
        console.log('Saved darbar_script.js');
        
    } catch (e) {
        console.error(e);
    }
}

fetchMenu();
