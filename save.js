// See https://github.com/dialogflow/dialogflow-fulfillment-nodejs
// for Dialogflow fulfillment library docs, samples, and to report issues
'use strict';
 
const functions = require('firebase-functions');
const {WebhookClient} = require('dialogflow-fulfillment');
const {Card, Suggestion} = require('dialogflow-fulfillment');
 
process.env.DEBUG = 'dialogflow:debug'; // enables lib debugging statements
 
exports.dialogflowFirebaseFulfillment = functions.https.onRequest((request, response) => {
  const agent = new WebhookClient({ request, response });
  console.log('Dialogflow Request headers: ' + JSON.stringify(request.headers));
  console.log('Dialogflow Request body: ' + JSON.stringify(request.body));
 
  function welcome(agent) {
    agent.add(`Welcome to my agent!`);
  }
 
  function fallback(agent) {
    agent.add(`I didn't understand`);
    agent.add(`I'm sorry, can you try again?`);
  }

    function nozawa(agent) {
        let event = agent.parameters['any'];
        let temp;
        let list = [];
        let i = 0;
        let j = 0;
        for(i = 0; i < event.length; i++){
            temp = event.substr(i, 1);
            list.push(temp);
        }
        list.push('ん');
    
        let a1 = [['あ', 'ア'], ['か', 'カ'], ['さ', 'サ'], ['た', 'タ'], ['な', 'ナ'], ['は', 'ハ'], ['ま', 'マ'], ['ら', 'ラ'],
                  ['が', 'ガ'], ['ざ', 'ザ'], ['だ', 'ダ'], ['ば', 'バ'], ['ぱ', 'パ']];
        let a2 = [['や', 'ヤ'], ['わ', 'ワ']];
        let ie = ['い', 'え', 'イ', 'エ'];
        let e = [['え', 'エ'], ['け', 'ケ'], ['せ', 'セ'], ['て', 'テ'], ['ね', 'ネ'], ['へ', 'へ'], ['め', 'メ'], ['れ', 'レ'], 
                 ['げ', 'ゲ'], ['ぜ', 'ゼ'], ['で', 'デ'], ['べ', 'ベ'], ['ぺ', 'ペ']];
    
        for(i = 0; i < list.length; i++){
            for(j = 0; j < a1.length; j++){
                if((list[i] == a1[j][0] || list[i] == a1[j][1]) && (list[i+1] == ie[0] || list[i+1] == ie[1] || list[i+1] == ie[2] || list[i+1] == ie[3])){
                list[i] = e[j][0];
                list[i+1] = 'ぇ';
                }
            }
            for(j = 0; j < a2.length; j++){
                if((list[i] == a2[j][0] || list[i] == a2[j][1]) && (list[i+1] == ie[0] || list[i+1] == ie[1] || list[i+1] == ie[2] || list[i+1] == ie[3])){
                list[i] = e[j][0];
                list[i+1] = 'ぇ';
                }
            }
            for(j = 0; j < e.length; j++){
                if((list[i] == e[j][0] || list[i] == e[j][1]) && (list[i+1] == ie[0] || list[i+1] == ie[1] || list[i+1] == ie[2] || list[i+1] == ie[3])){
                list[i+1] = 'ぇ';
                }
            }
            for(j = 0; j < e.length; j++){
                if((list[i] == e[j][0] || list[i] == e[j][1]) && list[i+1] == 'ー'){
                list[i+1] = 'ぇ';
                }
            }
            if((list[i] == 'お' && list[i+1] == 'れ') || (list[i] == 'ぼ' && list[i+1] == 'く')){
                list[i] == 'お';
                list[i+1] =='ら';
            }
        }
    
        list.pop();
        let list_changed = list.join('');
        agent.add(list_changed);
    }

  // // Uncomment and edit to make your own intent handler
  // // uncomment `intentMap.set('your intent name here', yourFunctionHandler);`
  // // below to get this function to be run when a Dialogflow intent is matched
  // function yourFunctionHandler(agent) {
  //   agent.add(`This message is from Dialogflow's Cloud Functions for Firebase editor!`);
  //   agent.add(new Card({
  //       title: `Title: this is a card title`,
  //       imageUrl: 'https://developers.google.com/actions/images/badges/XPM_BADGING_GoogleAssistant_VER.png',
  //       text: `This is the body text of a card.  You can even use line\n  breaks and emoji! 💁`,
  //       buttonText: 'This is a button',
  //       buttonUrl: 'https://assistant.google.com/'
  //     })
  //   );
  //   agent.add(new Suggestion(`Quick Reply`));
  //   agent.add(new Suggestion(`Suggestion`));
  //   agent.setContext({ name: 'weather', lifespan: 2, parameters: { city: 'Rome' }});
  // }

  // // Uncomment and edit to make your own Google Assistant intent handler
  // // uncomment `intentMap.set('your intent name here', googleAssistantHandler);`
  // // below to get this function to be run when a Dialogflow intent is matched
  // function googleAssistantHandler(agent) {
  //   let conv = agent.conv(); // Get Actions on Google library conv instance
  //   conv.ask('Hello from the Actions on Google client library!') // Use Actions on Google library
  //   agent.add(conv); // Add Actions on Google library responses to your agent's response
  // }
  // // See https://github.com/dialogflow/dialogflow-fulfillment-nodejs/tree/master/samples/actions-on-google
  // // for a complete Dialogflow fulfillment library Actions on Google client library v2 integration sample

  // Run the proper function handler based on the matched Dialogflow intent name
  let intentMap = new Map();
  intentMap.set('Default Welcome Intent', welcome);
  intentMap.set('Default Fallback Intent', fallback);
  intentMap.set('nozawa', nozawa);
  // intentMap.set('your intent name here', yourFunctionHandler);
  // intentMap.set('your intent name here', googleAssistantHandler);
  agent.handleRequest(intentMap);
});
