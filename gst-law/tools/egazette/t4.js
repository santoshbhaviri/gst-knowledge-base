const base = require('./t1.js'); const fs=require('fs');
module.exports = async (page) => {
  await base(page).catch(()=>{});
  await Promise.all([page.waitForURL(/SearchMinistry/,{waitUntil:'domcontentloaded', timeout:180000}), page.click('#btnMinistry')]);
  await page.waitForSelector('#ddlMinistry', {timeout:120000});
  for (const m of (process.env.MONTHS||'10').split(',')) {
    await page.selectOption('#ddlMinistry','18'); await page.waitForTimeout(3000);
    await page.check('#rdb_Option_0').catch(()=>{}); await page.waitForTimeout(2000);
    await page.selectOption('#ddlmonth', m); await page.selectOption('#ddlyear', process.env.YEAR||'2026');
    await Promise.all([page.waitForLoadState('domcontentloaded'), page.click('#ImgSubmitDetails')]);
    await page.waitForTimeout(10000);
    const html = await page.content(); fs.writeFileSync(process.env.S+'/eg_'+(process.env.YEAR||'2026')+'_'+m+'.html', html);
    console.log('MONTH', m, page.url(), (await page.innerText('body')).length);
    if (process.env.ONE) break;
    await page.goBack({waitUntil:'domcontentloaded'}).catch(()=>{}); await page.waitForTimeout(3000);
  }
};
