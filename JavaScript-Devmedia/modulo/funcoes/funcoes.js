const times_regiao = (times) => {   

    console.log("Todos os times:");
    times.forEach(time => {
    console.log(`${time.nome}`);
    })

    const timesRJ = times.filter(time => time.estado === 'RJ');
    console.log("\nTimes do RJ:");
    timesRJ.forEach(time => {
        console.log(`${time.nome}`);
    })

    const timesNE = times.filter(time => time.estado === 'CE' || time.estado === 'BA');
    console.log("\nTimes do Nordeste:");
    timesNE.forEach(time => {
        console.log(`${time.nome}`);
    })

    const timesSP = times.filter(time => time.estado === 'SP');
    console.log("\nTimes de São Paulo:");
    timesSP.forEach(time => {
        console.log(`${time.nome}`);
    })

    const timesSUL = times.filter(time => time.estado === 'PR' || time.estado === 'RS');
    console.log("\nTimes do Sul:");
    timesSUL.forEach(time => {
        console.log(`${time.nome}`);
    })

    const timesMGMS = times.filter(time => time.estado === 'MG' || time.estado === 'MS');
    console.log("\nTimes de MG e Centro-Oeste:");
    timesMGMS.forEach(time => {
        console.log(`${time.nome}`);
        
    })
}

export default {times_regiao};
// module.exports = {
//     times_regiao
// }