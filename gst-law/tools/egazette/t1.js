const dump = async (page) => { console.log('URL', page.url()); console.log((await page.innerText('body')).slice(0, 2000));
  const links = await page.$$eval('a,input[type=submit],input[type=image],select,input[type=radio],input[type=text]', els => els.map(e => e.tagName+' '+(e.id||e.name)+' '+(e.innerText||e.value||'').slice(0,60).replace(/\s+/g,' ')));
  console.log(links.join('\n')); };
module.exports = async (page) => {
  await page.goto('https://egazette.gov.in/', { timeout: 120000, waitUntil:'commit' }); await page.waitForURL(/default/i, {timeout:120000, waitUntil:'domcontentloaded'});
  await Promise.all([page.waitForURL(/SearchMenu/i,{timeout:120000, waitUntil:'domcontentloaded'}), page.click('a[href="SearchMenu.aspx"] >> nth=0')]);
  await dump(page);
};
module.exports.dump = dump;
