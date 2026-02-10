# -*- coding: utf-8 -*-
path = 'index.html'
with open(path, 'r', encoding='utf-8') as f:
    s = f.read()

# eNeuro
old1 = '''<p class="paper-summary">Using dendritic cable simulations with a calcium-based synapse model (NMDA receptors and VGCCs), we show that voltage attenuates asymmetrically along the dendrite: distal sites see larger depolarization from a proximal NMDA spike than do proximal sites. This asymmetry produces hierarchical heterosynaptic plasticity—e.g. an NMDA spike on a proximal branch can induce plasticity mainly on distal branches. We also study how simultaneous activation at multiple sites affects plasticity at active and "sandwiched" synapses. <a href="https://github.com/mkblitz/Hierarchical-hetero" target="_blank" rel="noopener">Code</a>.</p>'''
new1 = '''<p class="paper-abstract">Long-term synaptic plasticity is mediated via cytosolic calcium concentrations ([Ca<sup>2+</sup>]). Using a synaptic model that implements calcium-based long-term plasticity via two sources of Ca<sup>2+</sup>—NMDA receptors and voltage-gated calcium channels (VGCCs)—we show in dendritic cable simulations that the interplay between these two calcium sources can result in a diverse array of heterosynaptic effects. When spatially clustered synaptic input produces a local NMDA spike, the resulting dendritic depolarization can activate VGCCs at nonactivated spines, resulting in heterosynaptic plasticity. NMDA spike activation at a given dendritic location will tend to depolarize dendritic regions that are located distally to the input site more than dendritic sites that are proximal to it. This asymmetry can produce a hierarchical effect in branching dendrites, where an NMDA spike at a proximal branch can induce heterosynaptic plasticity primarily at branches that are distal to it. We also explored how simultaneously activated synaptic clusters located at different dendritic locations synergistically affect the plasticity at the active synapses, as well as the heterosynaptic plasticity of an inactive synapse "sandwiched" between them. We conclude that the inherent electrical asymmetry of dendritic trees enables sophisticated schemes for spatially targeted supervision of heterosynaptic plasticity.</p>
              <p><a href="https://github.com/mkblitz/Hierarchical-hetero" target="_blank" rel="noopener">Code</a></p>'''
# Use unicode for curly quotes in old
old1 = old1.replace('"', '\u201c').replace('"', '\u201d')
# But our old1 has straight " in "sandwiched" - so only the closing one might be curly. Check file.
# Actually in the file we have " and " (curly). So in Python we need \u201c and \u201d in old1.
if old1 in s:
    s = s.replace(old1, new1)
    print('eNeuro ok')
else:
    # Try with straight quotes
    old1_straight = '''<p class="paper-summary">Using dendritic cable simulations with a calcium-based synapse model (NMDA receptors and VGCCs), we show that voltage attenuates asymmetrically along the dendrite: distal sites see larger depolarization from a proximal NMDA spike than do proximal sites. This asymmetry produces hierarchical heterosynaptic plasticity—e.g. an NMDA spike on a proximal branch can induce plasticity mainly on distal branches. We also study how simultaneous activation at multiple sites affects plasticity at active and "sandwiched" synapses. <a href="https://github.com/mkblitz/Hierarchical-hetero" target="_blank" rel="noopener">Code</a>.</p>'''
    if old1_straight in s:
        s = s.replace(old1_straight, new1)
        print('eNeuro ok (straight)')
    else:
        print('eNeuro not found')

# G-clusteron - file has "dendrite" with curly quotes
old2 = '<p class="paper-summary">We introduce the gradient clusteron (G-clusteron): a model neuron whose synapses lie on a one-dimensional "dendrite" and interact'
old2_curly = old2.replace('"', '\u201c').replace('"', '\u201d')
new2_start = '<p class="paper-abstract">Synaptic clustering on neuronal dendrites has been hypothesized to play an important role in implementing pattern recognition. Neighboring synapses on a dendritic branch can interact in a synergistic, cooperative manner via nonlinear voltage-dependent mechanisms, such as NMDA receptors. Inspired by the NMDA receptor, the single-branch clusteron learning algorithm takes advantage of location-dependent multiplicative nonlinearities to solve classification tasks by randomly shuffling the locations of "under-performing" synapses on a model dendrite during learning ("structural plasticity"), eventually resulting in synapses with correlated activity being placed next to each other on the dendrite. We propose an alternative model, the gradient clusteron, or G-clusteron, which uses an analytically-derived gradient descent rule where synapses are "attracted to" or "repelled from" each other in an input- and location-dependent manner. We demonstrate the classification ability of this algorithm by testing it on the MNIST handwritten digit dataset and show that, when using a softmax activation function, the accuracy of the G-clusteron on the all-versus-all MNIST task (~85%) approaches that of logistic regression (~93%). In addition to the location update rule, we also derive a learning rule for the synaptic weights of the G-clusteron ("functional plasticity") and show that a G-clusteron that utilizes the weight update rule can achieve ~89% accuracy on the MNIST task. We also show that a G-clusteron with both the weight and location update rules can learn to solve the XOR problem from arbitrary initial conditions.</p>\n              <p><a href="https://github.com/mkblitz/The-Gradient-Clusteron" target="_blank" rel="noopener">Code</a></p>'
if old2 in s or old2_curly in s:
    s = s.replace(old2_curly if old2_curly in s else old2, new2_start)
    # Now remove the rest of the old G-clusteron paragraph (from "via a distance" to "</p>")
    import re
    s = re.sub(r'via a distance-dependent nonlinearity \(inspired by NMDA\). We derive a gradient-descent rule for synaptic <em>locations</em> so that synapses attract or repel depending on input and label\. With location updates only, the G-clusteron reaches ~85% on MNIST \(softmax\); with an additional weight-update rule it reaches ~89%\. With both rules it can learn XOR from arbitrary initial conditions\. <a href="https://github.com/mkblitz/The-Gradient-Clusteron" target="_blank" rel="noopener">Code</a>\.</p>', '', s, count=1)
    print('G-clusteron ok')
else:
    print('G-clusteron not found')

# JOCN
old3 = '<p class="paper-summary">We test whether implicit statistical learning of tone sequences (transition probabilities) affects what is held in auditory working memory and how the brain responds to violations. Using event-related potentials (ERPs) in response to melodies with statistically cohesive patterns, we show that statistical learning of melodic structure influences the brain's response to "wrong" notes, linking statistical learning to neurophysiological measures of expectation and memory.</p>'
old3_curly = old3.replace('"', '\u201c').replace('"', '\u201d')
new3 = '<p class="paper-abstract">Statistical learning is a fundamental mechanism that allows the brain to automatically extract structure from the environment. We examined whether implicit statistical learning of melodic patterns influences what is held in auditory working memory and the brain\'s response to violations of that structure. Event-related potentials (ERPs) were recorded in response to tone sequences that contained statistically cohesive melodic patterns. We found that statistical learning of melodic patterns influences the brain\'s response to "wrong" notes, demonstrating a direct link between statistical learning and neurophysiological measures of expectation and memory.</p>'
if old3 in s or old3_curly in s:
    s = s.replace(old3_curly if old3_curly in s else old3, new3)
    print('JOCN ok')
else:
    print('JOCN not found')

with open(path, 'w', encoding='utf-8') as f:
    f.write(s)
