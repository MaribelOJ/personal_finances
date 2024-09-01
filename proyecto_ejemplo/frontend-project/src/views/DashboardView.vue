<script setup >
    import FooterCom from '../components/Dashboard/FooterCom.vue';
    import Sidebar from '../components/Dashboard/Sidebar.vue';
    import Topbar from '../components/Dashboard/Topbar.vue';
    import UserProfile from '../components/Users/UserProfile.vue';
    import BlankPage from '../components/Dashboard/BlankPage.vue';
</script>

<template>
    <div id="wrapper">
        <Sidebar />

        <div id="content-wrapper" class="d-flex flex-column">
            <!-- Main Content -->
            <div id="content">
                <Topbar />
                <BlankPage></BlankPage>
            </div>
            <FooterCom />
        </div>
    </div>
</template>