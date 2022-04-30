<script>
    import { page } from '$app/stores';

    const id = $page.params.id;

    import { firebaseConfig } from "$lib/firebase";
    import { initializeApp } from "firebase/app";
    import { getFirestore, doc, getDoc } from "firebase/firestore";

    const fb = initializeApp(firebaseConfig);
    const db = getFirestore(fb);

    async function getEvent(id) {
        const docRef = doc(db, "Events", id);
        return await getDoc(docRef);
    }
</script>

{#await getEvent(id)}
    Loading Event...
{:then ev}


    <div class="relative top-12 max-w-3xl flex flex-col justify-center">
        <div class="">
            <div class="text-xl">Event: {ev.data().Title}</div>
            <div>When: {ev.data().Date.toDate()} </div>
            <div>Where: {ev.data().Location}</div>
            <div>What: {ev.data().Description}</div>
        </div>
        <div class="pt-12">
            We're just getting started! Sign-ups will be open soon
        </div>
    </div>
{/await}