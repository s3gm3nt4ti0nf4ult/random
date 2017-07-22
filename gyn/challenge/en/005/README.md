###### EN: Mission 005

Link to task:

[click](http://gynvael.vexillium.org/ext/thepicture/)

```
Welcome back agent 1336.
No mail.
> mission --take
MISSION 005               goo.gl/bOKTpd             DIFFICULTY: █████░░░░░ [5╱10]
┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅

We've already learned not to rely on "agent Huffman's" ability to send us text
messages. So this time, we've asked him to take a picture of some secret
documents and put them on a website. I mean, would could possibly go wrong,
right?

Well, he sent us this link:

  http://gynvael.vexillium.org/ext/thepicture/

Obviously we can't make heads or tails of it. Please help.

On a totally unrelated note, we're looking for new agents...

GOOD LUCK!

If you decode the answer, put it in the comments under this video! If you write
a blogpost / post your solution online, please add a link in the comments too!

P.S. I'll show/explain the solution on the stream next week.

```


My solution:

1. Given address redirect us to some page. In all my web browsers, there is only this icon available: ![resource](gyn/challenge/en/005/resource.png) This usually means broken image, or unavailable resource.
2. Viewing the source of that webpage gives us interesting message left by agent:

    ```
    <!-- Note: some browsers like Chrome, Firefox, IE, Safair, Edge, etc
         might not support this type of HTTP compression and image format.
         Actually, I don't think any browser supports it.
         It's perfect security!
    -->
    ```

    So the clue is obvoius. Check encoding and then do try to create file from that.
3. Running ` curl -v http://gynvael.vexillium.org/ext/thepicture/picture.image`
Gives us great perspective about encoding. 
