import streamlit as st
import streamlit.components.v1 as components

# Streamlit setup
st.set_page_config(page_title="Simulation", page_icon="🤖", layout="wide")

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        body { margin: 0; }
        canvas { display: block; }
        #controls {
            position: absolute;
            top: 10px;
            left: 10px;
            z-index: 100;
            background: rgba(255, 255, 255, 0.8);
            padding: 10px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div id="controls">
        <label for="joint1">Joint 1 Rotation:</label>
        <input type="range" id="joint1" name="joint1" min="-180" max="180" value="0">
        <br>
        <label for="joint2">Joint 2 Rotation:</label>
        <input type="range" id="joint2" name="joint2" min="-180" max="180" value="0">
        <br>
        <label for="joint3">Joint 3 Rotation:</label>
        <input type="range" id="joint3" name="joint3" min="-180" max="180" value="0">
        <br>
        <label for="joint4">Joint 4 Rotation:</label>
        <input type="range" id="joint4" name="joint4" min="-180" max="180" value="0">
        <br>
        <label for="joint5">Joint 5 Rotation:</label>
        <input type="range" id="joint5" name="joint5" min="-180" max="180" value="0">
        <br>
        <label for="joint6">Joint 6 Rotation:</label>
        <input type="range" id="joint6" name="joint6" min="-180" max="180" value="0">
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/GLTFLoader.js"></script>

    <script>
        let scene, camera, renderer, controls, model;
        const joints = {};

        init();
        animate();

        function init() {
            // Scene
            scene = new THREE.Scene();
            
            // Camera
            camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 2000);
            camera.position.set(0, 2, 80);  // Move the camera further back
            
            // Renderer
            renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.body.appendChild(renderer.domElement);
            
            // Orbit Controls
            controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true; // an animation loop is required when either damping or auto-rotation are enabled
            controls.dampingFactor = 0.25;
            controls.screenSpacePanning = false;
            controls.minDistance = 10;
            controls.maxDistance = 200; // Allow the camera to move even further back
            controls.maxPolarAngle = Math.PI;  // Allow full rotation around the vertical axis
            
            // Lights
            const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
            scene.add(ambientLight);
            const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
            directionalLight.position.set(10, 10, 10);
            scene.add(directionalLight);

            // GLTF Loader
            const loader = new THREE.GLTFLoader();
            loader.load('/static/irb120.gltf', function (gltf) {
                model = gltf.scene;

                // Scale the model down
                model.scale.set(0.5, 0.5, 0.5); 

                // Center the model
                model.position.set(0, 0, 0);

                scene.add(model);

                // Find and store joints
                joints.obj1 = model.getObjectByName('obj1');
                joints.obj2 = model.getObjectByName('obj2');
                joints.obj3 = model.getObjectByName('obj3');
                joints.obj4 = model.getObjectByName('obj4');
                joints.obj5 = model.getObjectByName('obj5');
                joints.obj6 = model.getObjectByName('obj6');
            });

            // Handle window resize
            window.addEventListener('resize', onWindowResize, false);

            // Slider event listeners
            document.getElementById('joint1').addEventListener('input', function(event) {
                const value = event.target.value;
                if (joints.obj1) {
                    joints.obj1.rotation.z = THREE.Math.degToRad(value);
                }
            });

            document.getElementById('joint2').addEventListener('input', function(event) {
                const value = event.target.value;
                if (joints.obj2) {
                    joints.obj2.rotation.z = THREE.Math.degToRad(value);
                }
            });

            document.getElementById('joint3').addEventListener('input', function(event) {
                const value = event.target.value;
                if (joints.obj3) {
                    joints.obj3.rotation.z = THREE.Math.degToRad(value);
                }
            });

            document.getElementById('joint4').addEventListener('input', function(event) {
                const value = event.target.value;
                if (joints.obj4) {
                    joints.obj4.rotation.z = THREE.Math.degToRad(value);
                }
            });

            document.getElementById('joint5').addEventListener('input', function(event) {
                const value = event.target.value;
                if (joints.obj5) {
                    joints.obj5.rotation.z = THREE.Math.degToRad(value);
                }
            });

            document.getElementById('joint6').addEventListener('input', function(event) {
                const value = event.target.value;
                if (joints.obj6) {
                    joints.obj6.rotation.z = THREE.Math.degToRad(value);
                }
            });
        }

        function onWindowResize() {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }

        function animate() {
            requestAnimationFrame(animate);

            controls.update(); // only required if controls.enableDamping = true, or if controls.autoRotate = true

            renderer.render(scene, camera);
        }
    </script>
</body>
"""

components.html(html_code, height=600)
